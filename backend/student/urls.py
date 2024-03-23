from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_students),
    path("<int:id>", views.get_student_courses),
]
