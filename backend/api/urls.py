from django.urls import include, path

from . import views
from account.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("user/register/", CreateUserView.as_view(), name="register"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("courses/", include("course.urls")),
    path("student/", include("student.urls")),
    # path("accounts/", include("account.urls")),
]
