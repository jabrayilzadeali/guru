from django.urls import path

from .views import (
    StudentBalanceAPIView,
    IncreaseStudentBalanceAPIView,
    PurchasedCoursesAPIView,
    CartListAPIView,
    PurchaseCartItemsCreateAPIView,
)
# PurchaseCreateAPIView,

urlpatterns = [
    path("balance/", StudentBalanceAPIView.as_view()),
    path("balance/increase/", IncreaseStudentBalanceAPIView.as_view()),
    path("purchased-courses/", PurchasedCoursesAPIView.as_view()),
    path("cart/", CartListAPIView.as_view()),
    # path("cart/add", CartListCreateAPIView.as_view()),
    # path("purchase-course/<int:pk>/", PurchaseCreateAPIView.as_view()),
    path("purchase-courses/", PurchaseCartItemsCreateAPIView.as_view()),
]
