from django.db.models import QuerySet

from course.models import Category


def category_list(*, limit: int = None) -> QuerySet[Category]:
    categories = Category.objects.filter(is_active=True)[:limit]
    return categories
