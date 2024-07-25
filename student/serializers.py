from rest_framework import serializers
from .models import Student, Purchase, Cart


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = "__all__"
        extra_kwargs = {"student": {"read_only": True}, "course": {"read_only": True}}


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"
        extra_kwargs = {"student": {"read_only": True}, "course": {"read_only": True}}
