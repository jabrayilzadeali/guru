from rest_framework import serializers
from .models import Course, CourseModule, CourseContent, CourseComment


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


class CourseModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModule
        fields = "__all__"
        extra_kwargs = {"user": {"read_only": True}, "course": {"read_only": True}}


class CourseCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseComment
        fields = "__all__"
        extra_kwargs = {"user": {"read_only": True}, "course": {"read_only": True}}
