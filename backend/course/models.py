from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField()

    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField(max_length=255)
    short_description = models.TextField(
        verbose_name="Short description",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Course(BaseModel):
    categories = models.ManyToManyField(
        Category,
        related_name="courses",
        related_query_name="courses",
    )
    title = models.CharField(max_length=255)
    short_description = models.TextField(
        verbose_name="Short description",
        blank=True,
        null=True,
    )
    long_description = models.TextField(
        verbose_name="Long description",
        blank=True,
        null=True,
    )
    image = models.ImageField(upload_to="uploads", blank=True, null=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"


class Lesson(BaseModel):
    class LessonStatus(models.TextChoices):
        DRAFT = "D", "draft"
        PUBLISHED = "P", "published"

    class LessonType(models.TextChoices):
        ARTICLE = "A", "article"
        QUIZ = "Q", "quiz"

    course = models.ForeignKey(
        Course,
        related_name="lessons",
        related_query_name="lessons",
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    short_description = models.TextField(
        verbose_name="Short description",
        blank=True,
        null=True,
    )
    long_description = models.TextField(
        verbose_name="Long description",
        blank=True,
        null=True,
    )
    status = models.CharField(choices=LessonStatus.choices, max_length=1)
    lesson_type = models.CharField(choices=LessonType.choices, max_length=1)

    def __str__(self) -> str:
        return self.title


class Comment(BaseModel):
    course = models.ForeignKey(
        Course,
        related_name="comments",
        related_query_name="comments",
        on_delete=models.CASCADE,
    )
    lesson = models.ForeignKey(
        Lesson,
        related_name="comments",
        related_query_name="comments",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=100)
    content = models.TextField()
    created_by = models.ForeignKey(
        User, related_name="comments", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.name
