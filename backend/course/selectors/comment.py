from django.db.models.query import QuerySet

from course.models import Comment


def comment_list(*, limit: int = None) -> QuerySet[Comment]:
    courses = Comment.objects.filter(is_active=True)[:limit]
    return courses


def comment_list_by_lesson(*, course_slug, lesson_slug):
    comments = comment_list().filter(lesson__slug=lesson_slug, course__slug=course_slug)
    print(comments)
    return comments
