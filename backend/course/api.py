from typing import List

from django.db.models.query import QuerySet
from rest_framework import serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from course.models import Course
from course.selectors.course import course_list, course_list_by_category_id


class CourseListApi(APIView):
    permission_classes = [AllowAny]

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        title = serializers.CharField()
        slug = serializers.SlugField()
        short_description = serializers.CharField()
        image = serializers.ImageField()

    def get(self, request):
        category_id: int = request.GET.get("category_id", None)

        courses: QuerySet[Course] = course_list_by_category_id(category_id=category_id)

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

    def get(self, request):
        courses = course_list(limit=4)
        serializer = self.OutputSerializer(
            courses, many=True, context={"request": request}
        )
        return Response(data=serializer.data)
