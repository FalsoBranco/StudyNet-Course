from typing import Any, Dict, List, Optional, Tuple

from django.contrib import admin
from django.db.models.fields.related import RelatedField
from django.db.models.query import QuerySet
from django.http.request import HttpRequest

from course.models import Category, Comment, Course, Lesson

# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    filter_horizontal = ("categories",)

    # Admin Options
    list_per_page = 13
    list_display = (
        "title",
        "slug",
        "created_at",
        "updated_at",
        "is_active",
    )
    search_fields = ("title",)
    list_filter = ("categories", "is_active")
    list_editable = ("is_active",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)

    # Admin Options
    list_per_page = 13
    list_editable = ("is_active",)
    list_display = (
        "title",
        "slug",
        "created_at",
        "updated_at",
        "is_active",
    )
    search_fields = ("title",)
    list_filter = ("is_active",)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    # Admin Options
    list_per_page = 13
    list_editable = ("is_active",)
    list_display = (
        "title",
        "slug",
        "course",
        "status",
        "lesson_type",
        "is_active",
    )
    list_filter = (
        "status",
        "lesson_type",
        "is_active",
    )
    search_fields = (
        "title",
        "short_description",
        "long_description",
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    # Admin Options
    list_per_page = 13
    list_display = (
        "course",
        "lesson",
        "name",
        "created_by",
        "created_at",
        "updated_at",
        "is_active",
    )
    search_fields = ("course", "lesson", "name")
    list_filter = ("is_active",)
