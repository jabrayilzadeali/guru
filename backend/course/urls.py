from django.urls import path

from . import views
from .views import (
    CourseListAPIView,
    CourseListCreateAPIView,
    CourseDetailAPIView,
    CourseUpdateAPIView,
    CourseDeleteAPIView,
    CourseModuleListAPIView,
    CourseContentListCreateAPIView,
    CourseCommentListAPIView,
    CourseCommentListMineAPIView,
    CourseCommentCreateAPIView,
    CourseCommentDetailAPIView,
    CourseCommentUpdateAPIView,
    CourseCommentDeleteAPIView,
)

urlpatterns = [
    # Courses
    path("", CourseListAPIView.as_view()),
    path("<int:pk>/", CourseDetailAPIView.as_view()),
    path("mine/", CourseListCreateAPIView.as_view()),
    path("mine/<int:pk>/", CourseDetailAPIView.as_view()),
    path("mine/<int:pk>/update/", CourseUpdateAPIView.as_view()),
    path("mine/<int:pk>/delete/", CourseDeleteAPIView.as_view()),
    # Course Modules
    path("<int:pk>/modules/", CourseModuleListAPIView.as_view()),
    # Course Contents
    path("mine/<int:pk>/contents/", CourseContentListCreateAPIView.as_view()),
    # Course Comments
    path("<int:pk>/comments/", CourseCommentListAPIView.as_view()),
    path("<int:pk>/comments/mine/", CourseCommentListMineAPIView.as_view()),
    path("<int:pk>/comments/create/", CourseCommentCreateAPIView.as_view()),
    path(
        "<int:pk>/comments/<int:id>/",
        CourseCommentDetailAPIView.as_view(),
    ),
    path(
        "<int:pk>/comments/<int:id>/update/",
        CourseCommentUpdateAPIView.as_view(),
    ),
    path(
        "<int:pk>/comments/<int:id>/delete/",
        CourseCommentDeleteAPIView.as_view(),
    ),
    # path("<int:pk>/comments/delete/", CourseCommentCreateAPIView.as_view()),
    # path(""),
    # path("", views.get_courses),
    # path("<int:id>/", views.get_course),
    # path("create/", views.create_course),
    # path("content/<int:id>/", views.get_content),
    # path("comments/<int:id>/", views.get_comments),
    # path("comments/<int:id1>/<int:id2>", views.get_comment),
    # path("create-comment/", views.create_comment),
    # path("purchases/", views.get_purchases),
]
