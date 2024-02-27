from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_courses),
    path("create-course/", views.create_course),
    path("<int:id>/", views.get_course),
]
