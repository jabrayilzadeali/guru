from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student, Purchase
from .serializers import StudentSerializer, PurchaseSerializer
from course.models import Course
from course.serializers import CourseSerializer
from rest_framework import status
from django.contrib.auth import get_user_model

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
def get_student_courses(request, id):
    try:
        user = User.objects.get(id=id)
        student = Student.objects.get(user=user)
        purchased_courses = Purchase.objects.filter(student=student)
        # courses = student.purchase_set.all()
        courses = Course.objects.filter(purchase__student=student)

    except Exception as e:
        raise e

    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)


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
