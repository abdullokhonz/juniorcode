from django.db import models


# Create your models here.


class Teachers(models.Model):
    objects = None
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    birth_date = models.DateField('Дата рождения', null=True, blank=True)
    bio = models.TextField('Биография', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return f'/teachers/teacher/{self.id}/detail'

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
