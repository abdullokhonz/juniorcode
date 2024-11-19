from django.shortcuts import render

# Create your views here.
from django.db.models import Q
from datetime import datetime
from django.shortcuts import render, redirect
from .models import Teachers
from .forms import TeachersForm
from django.views.generic import DetailView, UpdateView, DeleteView


# Create your views here.


def all_teachers(request):
    query = request.GET.get('q', '')
    search_field = request.GET.get('search_field', 'all')

    if not query and search_field == 'all':
        query = ''

    sort_field = request.GET.get('sort_field', 'id')
    sort_order = request.GET.get('sort_order', 'asc')

    teachers = Teachers.objects.all()

    if query:
        query_is_number = query.isdigit()

        if search_field == 'all':
            teachers = Teachers.objects.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                (Q(id__exact=int(query)) if query_is_number else Q()) |
                (Q(birth_date__exact=datetime.strptime(query, "%d.%m.%Y").date()) if query and query.count(
                    '.') == 2 else Q())
            )

        # Поиск по другим полям
        elif search_field == 'first_name':
            teachers = Teachers.objects.filter(first_name__icontains=query)
        elif search_field == 'last_name':
            teachers = Teachers.objects.filter(last_name__icontains=query)
        elif search_field == 'id' and query_is_number:
            teachers = Teachers.objects.filter(id__exact=int(query))
        elif search_field == 'birth_date':
            try:
                birth_date = datetime.strptime(query, "%d.%m.%Y").date()
                teachers = Teachers.objects.filter(birth_date=birth_date)
            except ValueError:
                teachers = Teachers.objects.none()
        else:
            teachers = Teachers.objects.all()

    if sort_field == 'id':
        teachers = teachers.order_by('id' if sort_order == 'asc' else '-id')
    elif sort_field == 'first_name':
        teachers = teachers.order_by('first_name' if sort_order == 'asc' else '-first_name')
    elif sort_field == 'last_name':
        teachers = teachers.order_by('last_name' if sort_order == 'asc' else '-last_name')
    elif sort_field == 'birth_date':
        teachers = teachers.order_by('birth_date' if sort_order == 'asc' else '-birth_date')

    return render(request, 'teachers/all_teachers.html', {
        'teachers': teachers,
        'query': query,
        'search_field': search_field,
        'sort_field': sort_field,
        'sort_order': sort_order
    })


def add_teacher(request):
    error = ''
    if request.method == 'POST':
        form = TeachersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_teachers')
        else:
            error = 'Форма была неверной!'

    form = TeachersForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'teachers/add_teacher.html', data)


class TeacherDetail(DetailView):
    model = Teachers
    template_name = 'teachers/teacher_detail.html'
    context_object_name = 'teacher'

    def get(self, request, *args, **kwargs):
        teacher = self.get_object()

        courses = teacher.courses.all()

        form = TeachersForm(instance=teacher, readonly=True)
        return render(request, self.template_name, {
            'form': form,
            'teacher': teacher,
            'courses': courses
        })


class TeacherUpdate(UpdateView):
    model = Teachers
    template_name = 'teachers/add_teacher.html'
    form_class = TeachersForm
    context_object_name = 'teacher'


class TeacherDelete(DeleteView):
    model = Teachers
    success_url = '/teachers/all'
    template_name = 'teachers/teacher_delete.html'
    context_object_name = 'teacher'
