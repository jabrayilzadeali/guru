from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Course, CourseComment
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import (
    CourseSerializer,
    CourseModuleSerializer,
    CourseContentSerializer,
    CourseCommentSerializer,
)


# Courses
class CourseListAPIView(generics.ListAPIView):
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]
    queryset = Course.objects.all()


class CourseDetailAPIView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = "pk"


class CourseListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Course.objects.filter(instructors=self.request.user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(instructors=[self.request.user])
            # serializer.save()
        else:
            print(serializer.errors)


class CourseUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "pk"

    def get_queryset(self):
        return Course.objects.filter(instructors=self.request.user)

    def get_update(self, serializer):
        serializer.save()


class CourseDeleteAPIView(generics.DestroyAPIView):
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "pk"

    def get_queryset(self):
        return Course.objects.filter(instructors=self.request.user)

    def get_destroy(self, instance):
        super().perform_destroy(instance)


class CourseModuleListAPIView(generics.ListAPIView):
    serializer_class = CourseModuleSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return Course.objects.get(pk=pk).coursemodule_set.all()


class CourseContentListCreateAPIView(generics.ListAPIView):
    serializer_class = CourseContentSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "pk"

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return Course.objects.get(pk=pk).coursecontent_set.all()

    # def perform_create(self, serializer):
    #     if serializer.is_valid():
    #         serializer.save(instructors=[self.request.user])
    #         # serializer.save()
    #     else:
    #         print(serializer.errors)


# Comments


class CourseCommentListAPIView(generics.ListAPIView):
    serializer_class = CourseCommentSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return Course.objects.get(pk=pk).coursecomment_set.all()


class CourseCommentListMineAPIView(generics.ListAPIView):
    serializer_class = CourseCommentSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return Course.objects.get(pk=pk).coursecomment_set.filter(
            user=self.request.user
        )


class CourseCommentCreateAPIView(generics.CreateAPIView):
    serializer_class = CourseCommentSerializer
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     return Course.objects.get(pk=pk).coursecomment_set.all()

    def perform_create(self, serializer):
        print("---------------------------------------------------------------")
        pk = self.kwargs.get("pk")
        Course.objects.get(pk=pk).coursecomment_set.all()
        if serializer.is_valid():
            serializer.save(user=self.request.user, course=Course.objects.get(pk=pk))
            # serializer.save()
        else:
            print(serializer.errors)


class CourseCommentDetailAPIView(generics.RetrieveAPIView):
    serializer_class = CourseCommentSerializer
    lookup_field = "id"

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        print(Course.objects.get(pk=pk))
        print(
            Course.objects.get(pk=pk).coursecomment_set.filter(user=self.request.user)
        )
        return Course.objects.get(pk=pk).coursecomment_set.filter(
            user=self.request.user
        )


class CourseCommentUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CourseCommentSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        print(
            Course.objects.get(pk=pk).coursecomment_set.filter(user=self.request.user)
        )
        return Course.objects.get(pk=pk).coursecomment_set.filter(
            user=self.request.user
        )

    def get_update(self, serializer):
        serializer.save()


class CourseCommentDeleteAPIView(generics.DestroyAPIView):
    serializer_class = CourseCommentSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        print(
            Course.objects.get(pk=pk).coursecomment_set.filter(user=self.request.user)
        )
        return Course.objects.get(pk=pk).coursecomment_set.filter(
            user=self.request.user
        )

    def get_destroy(self, instance):
        super().perform_destroy(instance)


# class CourseListCreateAPIView(generics.ListCreateAPIView):
#     serializer_class = CourseSerializer
#     permission_classes = [IsAuthenticated]
#
#     def get_queryset(self):
#         return Course.objects.filter(instructors=self.request.user)
#
#     def perform_create(self, serializer):
#         if serializer.is_valid():
#             serializer.save(instructors=[self.request.user])
#             # serializer.save()
#         else:
#             print(serializer.errors)


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
