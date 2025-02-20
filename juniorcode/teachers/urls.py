from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.all_teachers, name='all_teachers'),
    path('add_teacher', views.add_teacher, name='add_teacher'),
    path('teacher/<int:pk>/detail', views.TeacherDetail.as_view(), name='teacher_detail'),
    path('teacher/<int:pk>/update', views.TeacherUpdate.as_view(), name='teacher_update'),
    path('teacher/<int:pk>/delete', views.TeacherDelete.as_view(), name='teacher_delete'),
]
