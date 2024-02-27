from django.urls import include, path

from . import views

urlpatterns = [
    path('courses/', include("course.urls"))
]
