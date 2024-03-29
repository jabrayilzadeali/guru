from django.urls import path

from . import views
from .views import CourseListView

urlpatterns = [
    path("", CourseListView.as_view()),
    # path("", views.get_courses),
    path("<int:id>/", views.get_course),
    path("create-course/", views.create_course),
    path("content/<int:id>/", views.get_content),
    path("comments/<int:id>/", views.get_comments),
    path("comments/<int:id1>/<int:id2>", views.get_comment),
    path("create-comment/", views.create_comment),
    # path("purchases/", views.get_purchases),
]
