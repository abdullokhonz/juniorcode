from django.db.models import Q
from datetime import datetime
from django.shortcuts import render, redirect
from .models import Courses
from students.models import Students
from teachers.models import Teachers
from .forms import CourseForm
from django.views.generic import DetailView, UpdateView, DeleteView


# Create your views here.


def all_courses(request):
    title: str = "JuniorCode — курсы"

    query = request.GET.get('q', '')
    search_field = request.GET.get('search_field', 'all')

    if not query and search_field == 'all':
        query = ''

    sort_field = request.GET.get('sort_field', 'id')
    sort_order = request.GET.get('sort_order', 'asc')

    courses = Courses.objects.all()

    if query:
        query_is_number = query.isdigit()

        if search_field == 'all':
            courses = Courses.objects.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                (Q(id__exact=int(query)) if query_is_number else Q()) |
                (Q(start_date__exact=datetime.strptime(query, "%d.%m.%Y").date()) if query and query.count(
                    '.') == 2 else Q()) |
                (Q(end_date__exact=datetime.strptime(query, "%d.%m.%Y").date()) if query and query.count(
                    '.') == 2 else Q())
            )

        elif search_field == 'name':
            courses = Courses.objects.filter(name__icontains=query)
        elif search_field == 'description':
            courses = Courses.objects.filter(description__icontains=query)
        elif search_field == 'id' and query_is_number:
            courses = Courses.objects.filter(id__exact=int(query))
        elif search_field == 'start_date':
            try:
                start_date = datetime.strptime(query, "%d.%m.%Y").date()
                courses = Courses.objects.filter(start_date=start_date)
            except ValueError:
                courses = Courses.objects.none()
        elif search_field == 'end_date':
            try:
                end_date = datetime.strptime(query, "%d.%m.%Y").date()
                courses = Courses.objects.filter(start_date=end_date)
            except ValueError:
                courses = Courses.objects.none()
        else:
            courses = Courses.objects.all()

    if sort_field == 'id':
        courses = courses.order_by('id' if sort_order == 'asc' else '-id')
    elif sort_field == 'name':
        courses = courses.order_by('name' if sort_order == 'asc' else '-name')
    elif sort_field == 'description':
        courses = courses.order_by('description' if sort_order == 'asc' else '-description')
    elif sort_field == 'start_date':
        courses = courses.order_by('start_date' if sort_order == 'asc' else '-start_date')
    elif sort_field == 'end_date':
        courses = courses.order_by('end_date' if sort_order == 'asc' else '-end_date')

    noindex: bool = True

    return render(request, 'courses/all_courses.html', {
        'title': title,
        'courses': courses,
        'query': query,
        'search_field': search_field,
        'sort_field': sort_field,
        'sort_order': sort_order,
        'noindex': noindex
    })


def add_course(request):
    error = ''
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_courses')
        else:
            error = 'Форма была неверной!'

    form = CourseForm()
    teachers = Teachers.objects.all()
    students = Students.objects.all()

    data = {
        'form': form,
        'error': error,
        'teachers': teachers,
        'students': students
    }

    return render(request, 'courses/add_course.html', data)


class CourseDetail(DetailView):
    model = Courses
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'

    def get(self, request, *args, **kwargs):
        course = self.get_object()  # Получаем объект курса
        students = course.students.all()  # Получаем студентов курса
        teachers = Teachers.objects.all()  # Получаем всех преподавателей

        # Создаем форму для объекта course
        form = CourseForm(instance=course, readonly=True)

        return render(request, self.template_name, {
            'form': form,
            'course': course,
            'students': students,
            'teachers': teachers,
        })


class CourseUpdate(UpdateView):
    model = Courses
    template_name = 'courses/add_course.html'
    form_class = CourseForm
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teachers'] = Teachers.objects.all()
        context['students'] = Students.objects.all()
        context['course'] = self.object
        return context


class CourseDelete(DeleteView):
    model = Courses
    success_url = '/courses/all'
    template_name = 'courses/course_delete.html'
    context_object_name = 'course'
