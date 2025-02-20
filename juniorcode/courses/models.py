from django.db import models
from students.models import Students  # Импортируем модель студентов
from teachers.models import Teachers  # Импортируем модель преподавателей


class Courses(models.Model):
    objects = None
    name = models.CharField('Название курса', max_length=100)
    description = models.TextField('Описание курса', null=True, blank=True)
    teacher = models.ForeignKey(Teachers, on_delete=models.SET_NULL, null=True, blank=True, related_name='courses')
    students = models.ManyToManyField(Students, related_name='courses', null=True, blank=True)
    start_date = models.DateField('Дата начала курса', null=True, blank=True)
    end_date = models.DateField('Дата окончания курса', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/courses/course/{self.id}/detail'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
