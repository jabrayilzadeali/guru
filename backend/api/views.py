from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CourseSerializer
from .models import Course

# Create your views here.
@api_view(['GET'])
def apiOverview(request):

    return Response()

@api_view(['GET'])
def courseList(request):
    courses = Course.objects.all()    
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def courseDetail(request, pk):
    course = Course.objects.get(id=pk)
    serializer = CourseSerializer(course, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def courseCreate(request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def courseUpdate(request, pk):
    course = Course.objects.get(id=pk)
    serializer = CourseSerializer(instance=course, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def courseDelete(request, pk):
    course = Course.objects.get(id=pk)
    course.delete()
    return Response('Course is deleted')