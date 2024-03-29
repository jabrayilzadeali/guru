from django.urls import path

from . import views
from .views import StudentCourses

urlpatterns = [
    # path("", StudentCourses.as_view()),
    # path("", views.get_students),
    path("purchased-courses/", views.get_student_purchased_courses),
    path("increase-balance/<int:amount>/", views.increase_student_balance),
    path("purchase-courses/", views.purchase_courses),
]
