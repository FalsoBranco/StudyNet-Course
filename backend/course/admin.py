from django.contrib import admin

from .models import Category, Comment, Course, Lesson

# Register your models here.


class CommentsInline(admin.StackedInline):
    model = Comment
    raw_id_fields = ["lesson"]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["title", "course", "status", "lesson_type"]
    list_filter = ["status", "lesson_type"]
    search_fields = ["title", "short_description", "long_description"]
    inlines = [
        CommentsInline,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
