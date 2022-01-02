from django.db.models.query import QuerySet

from course.models import Lesson


def lesson_list(*, limit: int = None) -> QuerySet[Lesson]:
    lessons = Lesson.objects.filter(is_active=True)[:limit]
    return lessons


def lesson_get(*, slug: str) -> Lesson:
    lesson: Lesson = lesson_list().get(slug=slug)

    return lesson
