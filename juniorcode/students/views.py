from django.db.models import Q
from datetime import datetime
from django.shortcuts import render, redirect
from .models import Students
from .forms import StudentsForm
from django.views.generic import DetailView, UpdateView, DeleteView


# Create your views here.


def all_students(request):
    title: str = "JuniorCode — студенты"

    query = request.GET.get('q', '')
    search_field = request.GET.get('search_field', 'all')

    if not query and search_field == 'all':
        query = ''

    sort_field = request.GET.get('sort_field', 'id')
    sort_order = request.GET.get('sort_order', 'asc')

    students = Students.objects.all()

    if query:
        query_is_number = query.isdigit()

        if search_field == 'all':
            students = Students.objects.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                (Q(id__exact=int(query)) if query_is_number else Q()) |
                (Q(birth_date__exact=datetime.strptime(query, "%d.%m.%Y").date()) if query and query.count(
                    '.') == 2 else Q())
            )

        elif search_field == 'first_name':
            students = Students.objects.filter(first_name__icontains=query)
        elif search_field == 'last_name':
            students = Students.objects.filter(last_name__icontains=query)
        elif search_field == 'id' and query_is_number:
            students = Students.objects.filter(id__exact=int(query))
        elif search_field == 'birth_date':
            try:
                birth_date = datetime.strptime(query, "%d.%m.%Y").date()
                students = Students.objects.filter(birth_date=birth_date)
            except ValueError:
                students = Students.objects.none()
        else:
            students = Students.objects.all()

    if sort_field == 'id':
        students = students.order_by('id' if sort_order == 'asc' else '-id')
    elif sort_field == 'first_name':
        students = students.order_by('first_name' if sort_order == 'asc' else '-first_name')
    elif sort_field == 'last_name':
        students = students.order_by('last_name' if sort_order == 'asc' else '-last_name')
    elif sort_field == 'birth_date':
        students = students.order_by('birth_date' if sort_order == 'asc' else '-birth_date')

    noindex: bool = True

    return render(request, 'students/all_students.html', {
        'title': title,
        'students': students,
        'query': query,
        'search_field': search_field,
        'sort_field': sort_field,
        'sort_order': sort_order,
        'noindex': noindex
    })


def add_student(request):
    error = ''
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_students')
        else:
            error = 'Форма была неверной!'

    form = StudentsForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'students/add_student.html', data)


class StudentDetail(DetailView):
    model = Students
    template_name = 'students/student_detail.html'
    context_object_name = 'student'

    def get(self, request, *args, **kwargs):
        student = self.get_object()

        courses = student.courses.all()

        form = StudentsForm(instance=student, readonly=True)

        return render(request, self.template_name, {
            'form': form,
            'student': student,
            'courses': courses
        })


class StudentUpdate(UpdateView):
    model = Students
    template_name = 'students/add_student.html'
    form_class = StudentsForm
    context_object_name = 'student'


class StudentDelete(DeleteView):
    model = Students
    success_url = '/students/all'
    template_name = 'students/student_delete.html'
    context_object_name = 'student'
