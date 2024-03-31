from rest_framework import serializers
from .models import Course, CourseContent, CourseComment


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
        extra_kwargs = {"instructors": {"read_only": True}}


class CourseContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseContent
        fields = "__all__"
        extra_kwargs = {"instructors": {"read_only": True}}


class CourseCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseComment
        fields = "__all__"
        extra_kwargs = {"instructors": {"read_only": True}}
