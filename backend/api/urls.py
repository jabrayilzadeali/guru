from django.urls import include, path

from . import views

urlpatterns = [
    path("courses/", include("course.urls")),
    path("students/", include("student.urls")),
    path("accounts/", include("account.urls")),
]
