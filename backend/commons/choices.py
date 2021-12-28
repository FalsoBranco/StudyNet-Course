from django.db import models


class LessonStatus(models.TextChoices):
    DRAFT = "D", "draft"
    PUBLISHED = "P", "published"


class LessonType(models.TextChoices):
    ARTICLE = "A", "article"
    QUIZ = "Q", "quiz"
