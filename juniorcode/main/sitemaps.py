from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from datetime import datetime
from courses.models import Courses
from students.models import Students
from teachers.models import Teachers


class StaticViewSitemap(Sitemap):
    def items(self):
        return [
            'main',
            'all_students',
            'all_teachers',
            'all_courses',
        ]

    def location(self, item):
        return reverse(item)

    def lastmod(self, item):
        return datetime.now()

    def changefreq(self, item):
        return 'weekly'

    def priority(self, item):
        return {
            'main': 1.0,
            'all_students': 0.9,
            'all_teachers': 0.9,
            'all_courses': 0.9,
        }.get(item, 0.8)


class StudentSitemap(Sitemap):
    def items(self):
        return Students.objects.all()

    def location(self, obj):
        return reverse('student_detail', args=[obj.pk])

    def lastmod(self, obj):
        return datetime.now()

    def changefreq(self, obj):
        return 'weekly'

    def priority(self, obj):
        return 0.7


class TeacherSitemap(Sitemap):
    def items(self):
        return Teachers.objects.all()

    def location(self, obj):
        return reverse('teacher_detail', args=[obj.pk])

    def lastmod(self, obj):
        return datetime.now()

    def changefreq(self, obj):
        return 'weekly'

    def priority(self, obj):
        return 0.7


class CourseSitemap(Sitemap):
    def items(self):
        return Courses.objects.all()

    def location(self, obj):
        return reverse('course_detail', args=[obj.pk])

    def lastmod(self, obj):
        return datetime.now()

    def changefreq(self, obj):
        return 'weekly'

    def priority(self, obj):
        return 0.8
