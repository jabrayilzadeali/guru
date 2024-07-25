from django.urls import include, path

from . import views
from account.views import CreateUserAPIView
from account.views import CustomTokenObtainPairView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("user/register/", CreateUserAPIView.as_view(), name="register"),
    path("user/login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("courses/", include("course.urls")),
    path("student/", include("student.urls")),
    path("stats/", include("stats.urls"))
    # path("auth/", include("rest_framework.urls")),
    # path("accounts/", include("account.urls")),
]
