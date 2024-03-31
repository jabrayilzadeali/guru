from django.urls import path

from . import views
from .views import CreateUserAPIView

urlpatterns = [
    path("all-users/", views.all_users),
    path("profile/", views.profile),
]
