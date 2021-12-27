from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Comment, Course, Lesson
from .serializers import (
    CategoryListSerializer,
    CommentListSerializer,
    CourseDetailSerializer,
    CourseListSerializer,
)

# Create your views here.


class CourseListApi(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    def get(self, request):
        category_id = request.GET.get("category_id")
        courses = Course.objects.all()
        if category_id:
            courses = courses.filter(categories__in=[int(category_id)])

        serializer = CourseListSerializer(
            courses, many=True, context={"request": request}
        )
        return Response(data=serializer.data)


class CourseDetailApi(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, courseSlug):
        course: Course = Course.objects.get(slug=courseSlug)

        serializer = CourseDetailSerializer(course).data
        # course_serializer = CourseDetailSerializer(course)
        # lesson_serializer = LessonListSerializer(course.lessons.all(), many=True)
        # data = {"course": course_serializer.data, "lessons": lesson_serializer.data}

        return Response(data=serializer)


class CommentAddApi(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, course_slug: str, lesson_slug: str):
        data = request.data
        name = data.get("name")
        content = data.get("content")

        course = get_object_or_404(Course, slug=course_slug)
        lesson = get_object_or_404(Lesson, slug=lesson_slug)
        print(request.user)
        comment = Comment.objects.create(
            course=course,
            lesson=lesson,
            name=name,
            content=content,
            created_by=request.user,
        )
        serializer = CommentListSerializer(comment)
        return Response(data=serializer.data)


class CommentListApi(APIView):
    def get(self, request, course_slug: str, lesson_slug: str):
        lesson = get_object_or_404(Lesson, slug=lesson_slug)
        comments = lesson.comments.all()
        serializer = CommentListSerializer(comments, many=True)
        data = serializer.data

        return Response(data=data)


class CourseNewFrontPageApi(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        courses = Course.objects.all()[:4]
        serializer = CourseListSerializer(
            courses, many=True, context={"request": request}
        )
        return Response(data=serializer.data)


class CategoryListApi(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategoryListSerializer(
            categories, many=True, context={"request": request}
        )
        return Response(data=serializer.data)
