from django.urls import path

from . import views
from .views import (
    CourseListAPIView,
    CourseListCreateAPIView,
    CourseDetailAPIView,
    CourseUpdateAPIView,
    CourseDeleteAPIView,
    CourseContentListCreateAPIView,
)

urlpatterns = [
    # Courses
    path("", CourseListAPIView.as_view()),
    path("<int:pk>/", CourseDetailAPIView.as_view()),
    path("mine/", CourseListCreateAPIView.as_view()),
    path("mine/<int:pk>/", CourseDetailAPIView.as_view()),
    path("mine/<int:pk>/update/", CourseUpdateAPIView.as_view()),
    path("mine/<int:pk>/delete/", CourseDeleteAPIView.as_view()),
    # Couse Content
    path("mine/<int:pk>/contents/", CourseContentListCreateAPIView.as_view()),
    # path("", views.get_courses),
    # path("<int:id>/", views.get_course),
    # path("create/", views.create_course),
    # path("content/<int:id>/", views.get_content),
    # path("comments/<int:id>/", views.get_comments),
    # path("comments/<int:id1>/<int:id2>", views.get_comment),
    # path("create-comment/", views.create_comment),
    # path("purchases/", views.get_purchases),
]
