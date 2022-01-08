from django.urls import path
from django.urls.conf import include

from course.api import (
    CategoryListApi,
    CommentAddApi,
    CommentListApi,
    CourseDetailApi,
    CourseListApi,
    CourseNewFrontPageApi,
    QuizGetApi,
)

app_name = "courses"

comments_urlpatterns = [
    path(
        "<slug:course_slug>/<slug:lesson_slug>/",
        CommentAddApi.as_view(),
        name="create",
    ),
    path(
        "<slug:course_slug>/<slug:lesson_slug>/get-comments/",
        CommentListApi.as_view(),
        name="list",
    ),
]

category_urlpatterns = [
    path(
        "",
        CategoryListApi.as_view(),
        name="list",
    ),
]

quiz_urlpatterns = [
    path(
        "<slug:course_slug>/<slug:lesson_slug>/get-quiz/",
        QuizGetApi.as_view(),
        name="get",
    ),
]

urlpatterns = [
    path("", CourseListApi.as_view(), name="list"),
    path("", include((comments_urlpatterns, "comments"))),
    path("", include((quiz_urlpatterns, "quizzes"))),
    path("categories/", include((category_urlpatterns, "categories"))),
    path("new-courses/", CourseNewFrontPageApi.as_view(), name="list"),
    path("<slug:course_slug>/", CourseDetailApi.as_view(), name="detail"),
]
