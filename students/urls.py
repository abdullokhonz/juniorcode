from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.all_students, name='all_students'),
    path('add_student', views.add_student, name='add_student'),
    path('student/<int:pk>/detail', views.StudentDetail.as_view(), name='student_detail'),
    path('student/<int:pk>/update', views.StudentUpdate.as_view(), name='student_update'),
    path('student/<int:pk>/delete', views.StudentDelete.as_view(), name='student_delete'),
]
