from django.urls import path

from course.api import CourseListApi, CourseNewFrontPageApi

from .views import (  # CourseListApi,; CourseNewFrontPageApi,
    CategoryListApi,
    CommentAddApi,
    CommentListApi,
    CourseDetailApi,
)

app_name = "courses"

urlpatterns = [
    path("", CourseListApi.as_view(), name="list"),
    path("categories/", CategoryListApi.as_view(), name="categories-list"),
    path("new-courses/", CourseNewFrontPageApi.as_view(), name="list"),
    path("<slug:courseSlug>/", CourseDetailApi.as_view(), name="detail"),
    path(
        "<slug:course_slug>/<slug:lesson_slug>/",
        CommentAddApi.as_view(),
        name="add-comment",
    ),
    path(
        "<slug:course_slug>/<slug:lesson_slug>/get-comments/",
        CommentListApi.as_view(),
        name="get-comment",
    ),
]
