from rest_framework import serializers

from .models import Category, Comment, Course, Lesson


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "title", "slug")


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("id", "title", "slug", "short_description", "image")


class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            "id",
            "title",
            "slug",
            "short_description",
            "long_description",
            "get_status_display",
        )


class CourseDetailSerializer(serializers.ModelSerializer):
    lessons = LessonListSerializer(many=True)

    class Meta:
        model = Course
        fields = (
            "id",
            "title",
            "slug",
            "lessons",
            "short_description",
            "long_description",
        )


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "name", "content", "created_at"]
