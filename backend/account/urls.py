from django.urls import path

from . import views

urlpatterns = [
    path("all-users/", views.all_users),
    path("signup/", views.signup),
]
