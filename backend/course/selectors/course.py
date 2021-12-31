from django.db.models.query import QuerySet

from course.models import Course


def course_list(*, limit: int = None) -> QuerySet[Course]:
    courses = Course.objects.filter(is_active=True)[:limit]
    return courses


def course_list_by_category_id(*, category_id: int = None) -> QuerySet[Course]:
    courses = course_list()
    if category_id is None:
        return courses

    return courses.filter(categories=category_id)
