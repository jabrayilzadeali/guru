from django.shortcuts import render
from rest_framework import status, generics
from .models import TeacherFinancialOverview, StudentLocation
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import TeacherFinancialOverviewSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
class TeacherFinancialOverviewListAPIView(generics.ListAPIView):
    serializer_class = TeacherFinancialOverviewSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        instructor_username = self.kwargs.get('instructor')
        instructor = User.objects.get(username=instructor_username)

        return TeacherFinancialOverview.objects.filter(instructor=instructor)
    
class StudentLocationListAPIView: 
    ...