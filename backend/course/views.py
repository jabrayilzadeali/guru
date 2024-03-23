from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Course, CourseComment
from rest_framework import status
from .serializers import CourseSerializer, CourseCommentSerializer


# Courses
@api_view(["GET"])
def get_courses(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    print("Authenticated User:", request.user)
    return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
def get_course(request, id):
    try:
        course = Course.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    if request.method == "PUT":
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    if request.method == "DELETE":
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
def create_course(request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


# Comments
@api_view(["GET"])
def get_comments(request, id):
    try:
        course = Course.objects.get(id=id)
        comments = course.coursecomment_set.all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = CourseCommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
def get_comment(request, id1, id2):
    try:
        course = Course.objects.get(id=id1)
        comment = course.coursecomment_set.get(id=id2)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = CourseCommentSerializer(comment)
        return Response(serializer.data)
    if request.method == "PUT":
        serializer = CourseCommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    if request.method == "DELETE":
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
def create_comment(request):
    print("okay")
    serializer = CourseCommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
