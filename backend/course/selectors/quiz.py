from django.db.models import QuerySet

from course.models import Quiz


def quiz_list(*, limit: int = None) -> QuerySet[Quiz]:
    quizzes = Quiz.objects.filter(is_active=True)[:limit]
    return quizzes


def quiz_get_by_lesson(*, lesson_slug: str = None) -> Quiz:
    quizzes = quiz_list().get(lesson__slug=lesson_slug)
    return quizzes
