from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student, Purchase, Cart
from .serializers import StudentSerializer, PurchaseSerializer
from course.models import Course
from course.serializers import CourseSerializer
from django.contrib.auth import get_user_model
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, AllowAny

User = get_user_model()


@api_view(["GET"])
def get_students(request):
    try:
        students = Student.objects.all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def increase_student_balance(request, amount):
    user = request.user
    print(user, amount)
    student, created = Student.objects.get_or_create(user=user)
    student.increase_balance(amount)
    serializer = StudentSerializer(student)
    return Response(serializer.data)


class StudentCourses(generics.ListAPIView):
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # user = self.request.user
        return Course.objects.all()


@api_view(["GET"])
def get_student_purchased_courses(request):
    try:
        user = request.user
        courses = Course.objects.filter(purchase__student__user=user)

    except Exception as e:
        raise e

    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(["GET", "POST"])
def purchase_courses(request):
    if request.method == "GET":
        user = request.user
        courses = Course.objects.exclude(purchase__student__user=user)
        # user = request.user
        # courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    if request.method == "Post":
        course_id = request.query_params.get("amount")


# @api_view(["GET"])
# def get_purchases(request):
#     try:
#         purchases = Purchase.objects.all()
#         print("cool")
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     serializer = PurchaseSerializer(purchases, many=True)
#     return Response(serializer.data)
