from django.urls import path
from . import views

urlpatterns = [
    path('all', views.all_courses, name='all_courses'),
    path('add_course', views.add_course, name='add_course'),
    path('course/<int:pk>/detail', views.CourseDetail.as_view(), name='course_detail'),
    path('course/<int:pk>/update', views.CourseUpdate.as_view(), name='course_update'),
    path('course/<int:pk>/delete', views.CourseDelete.as_view(), name='course_delete')
]
