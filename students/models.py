from django.db import models


# Create your models here.


class Students(models.Model):
    objects = None
    first_name = models.CharField('Имя', max_length=25)
    last_name = models.CharField('Фамилия', max_length=25)
    birth_date = models.DateField('Дата рождения', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return f'/students/student/{self.id}/detail'

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
