from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student, Purchase, Cart
from .serializers import StudentSerializer, CartSerializer, PurchaseSerializer
from course.models import Course
from course.serializers import CourseSerializer
from django.contrib.auth import get_user_model
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db.models import Sum

User = get_user_model()


# @api_view(["GET"])
# def get_students(request):
#     try:
#         students = Student.objects.all()
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     serializer = StudentSerializer(students, many=True)
#     return Response(serializer.data)


class StudentBalanceAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # student = request.user.student
        user = request.user
        student, created = Student.objects.get_or_create(user=user)
        serializer = StudentSerializer(student)
        return Response(serializer.data)


class IncreaseStudentBalanceAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        amount = request.data.get("amount")
        user = request.user
        student, created = Student.objects.get_or_create(user=user)
        student.increase_balance(amount)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    # def post(self, request):
    #     amount = request.data.get('amount')
    #     student = request.user.student
    #     student.increase_balance(amount)
    #     serializer = StudentSerializer(student)
    #     return Response(serializer.data)


class PurchasedCoursesAPIView(generics.ListAPIView):
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        student = generics.get_object_or_404(Student, user=self.request.user)
        return Purchase.objects.filter(student=student)


class CartListAPIView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        student = generics.get_object_or_404(Student, user=self.request.user)
        return Cart.objects.filter(student=student)


class PurchaseCartItemsCreateAPIView(generics.CreateAPIView):
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if serializer.is_valid():
            user = self.request.user
            student = Student.objects.get(user=user)

            # cart_items = Cart.objects.filter(
            #     student=student).aggregate(Sum("course__price"))
            #
            # total_price = cart_total.get("course__price__sum") or 0
            cart_items = Cart.objects.filter(student=student)
            total_price = sum(item.course.price for item in cart_items)
            if student.balance >= total_price:
                for cart_item in cart_items:
                    Purchase.objects.create(
                        student=student, course=cart_item.course)
                print("balance: ", student.balance, "total_price", total_price)
                # student.balance -= total_price
                # print(student.balance)
                # student.save()
                cart_items.delete()  # Remove items from the cart after purchase
                return Response({"message": "Purchase successful"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "Insufficient balance"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            print(serializer.errors)


class PurchaseCreateAPIView(generics.CreateAPIView):
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(student__user=self.request.user)
            # serializer.save()
        else:
            print(serializer.errors)
# @api_view(["GET"])
# def get_student_purchased_courses(request):
#     try:
#         user = request.user
#         courses = Course.objects.filter(purchase__student__user=user)
#
#     except Exception as e:
#         raise e
#
#     serializer = CourseSerializer(courses, many=True)
#     return Response(serializer.data)


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
