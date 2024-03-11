from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_courses),
    path("<int:id>/", views.get_course),
    path("create-course/", views.create_course),
    path("comments/<int:id>/", views.get_comments),
    path("comments/<int:id1>/<int:id2>", views.get_comment),
    path("create-comment/", views.create_comment),
]
