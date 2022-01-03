from commons.utils import inline_serializer
from django.urls import reverse
from rest_framework import serializers
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from course.selectors.category import category_list
from course.selectors.comment import comment_list_by_lesson
from course.selectors.course import (
    course_detail,
    course_get,
    course_list,
    course_list_by_category_id,
)
from course.selectors.lesson import lesson_get
from course.services.comment import comment_create


class CategoryListApi(APIView):
    permission_classes = [AllowAny]

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        title = serializers.CharField()
        slug = serializers.CharField()

    def get(self, request: Request) -> Response:
        categories = category_list()
        serializer = self.OutputSerializer(categories, many=True)
        return Response(data=serializer.data)


class CourseListApi(APIView):
    permission_classes = [AllowAny]

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        title = serializers.CharField()
        slug = serializers.SlugField()
        short_description = serializers.CharField()
        image = serializers.ImageField()

    def get(self, request: Request) -> Response:
        category_id: str = request.GET.get("category_id", None)

        courses = course_list_by_category_id(category_id=category_id)

        serializer = self.OutputSerializer(
            courses, many=True, context={"request": request}
        )
        return Response(data=serializer.data)


class CourseNewFrontPageApi(APIView):
    permission_classes = [AllowAny]

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        title = serializers.CharField()
        slug = serializers.SlugField()
        short_description = serializers.CharField()
        image = serializers.ImageField()

    def get(self, request: Request) -> Response:
        courses = course_list(limit=4)
        serializer = self.OutputSerializer(
            courses, many=True, context={"request": request}
        )
        return Response(data=serializer.data)


class CourseDetailApi(APIView):
    class OutputSerializer(serializers.Serializer):
        title = serializers.CharField()
        long_description = serializers.CharField()
        lessons = inline_serializer(
            many=True,
            fields={
                "title": serializers.CharField(),
                "slug": serializers.CharField(),
                "long_description": serializers.CharField(),
            },
        )

    def get(self, request: Request, course_slug: str) -> Response:

        course = course_detail(slug=course_slug)
        serializer = self.OutputSerializer(course, context={"request", request})
        # course_serializer = CourseDetailSerializer(course)
        # lesson_serializer = LessonListSerializer(course.lessons.all(), many=True)
        # data = {"course": course_serializer.data, "lessons": lesson_serializer.data}
        return Response(data=serializer.data)


class CommentListApi(APIView):
    permission_classes = [IsAuthenticated]

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField()
        content = serializers.CharField()

    def get(self, request: Request, course_slug: str, lesson_slug: str) -> Response:
        comments = comment_list_by_lesson(
            course_slug=course_slug, lesson_slug=lesson_slug
        )
        serializer = self.OutputSerializer(comments, many=True)
        return Response(data=serializer.data)


class CommentAddApi(APIView):
    permission_classes = [IsAuthenticated]

    class InputSerializer(serializers.Serializer):
        name = serializers.CharField()
        content = serializers.CharField()

    class ResponseSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField()
        content = serializers.CharField()

    def post(self, request: Request, course_slug: str, lesson_slug: str):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        course = course_get(slug=course_slug)
        lesson = lesson_get(slug=lesson_slug)
        comment = comment_create(
            **serializer.validated_data,
            user=request.user,
            lesson=lesson,
            course=course,
        )
        serializer_response = self.ResponseSerializer(comment)

        return Response(data=serializer_response.data)
