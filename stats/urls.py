from django.urls import path
from .views import TeacherFinancialOverviewListAPIView, StudentLocationListAPIView


urlpatterns = [
    path("teacher-financial-overview/<str:instructor>", TeacherFinancialOverviewListAPIView.as_view()),
    # path("student-location", StudentLocationListAPIView.as_view()),
]