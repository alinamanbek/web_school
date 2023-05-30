from django.urls import path, include
from rest_framework import routers
from .views import TeacherViewSet, StudentViewSet, CourseViewSet
from .views import delete_teacher, delete_student, create_teacher, create_student, create_course,delete_course

router = routers.DefaultRouter()
router.register(r'teachers', TeacherViewSet)
router.register(r'students', StudentViewSet)
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('teachers/<int:teacher_id>/', delete_teacher, name='delete_teacher'),
    path('students/<int:student_id>/', delete_student, name='delete_student'),
    path('courses/<int:courses_id>/', delete_course, name='delete_course'),
    path('api/teachers/', create_teacher, name='create_teacher'),
    path('api/students/', create_student, name='create_student'),
    path('api/courses/', create_course, name='create_course'),
]

