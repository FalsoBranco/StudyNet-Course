from accounts.models import CustomUser as User
from commons.choices import LessonStatus, LessonType
from commons.models import BaseModel
from django.db import models

# Create your models here.
# TODO slug in course/lesson


class Category(BaseModel):
    title = models.CharField(
        max_length=100,
        verbose_name="Category name",
        help_text="format: required, max-100",
        null=False,
        unique=False,
        blank=False,
    )
    slug = models.SlugField(
        max_length=150,
        verbose_name="category safe URL",
        help_text="format: required, letters, numbers, underscore, or hyphens",
        null=False,
        unique=False,
        blank=True,
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        ordering = ["title", "-created_at"]


class Course(BaseModel):
    categories = models.ManyToManyField(
        Category,
        related_name="categories",
    )
    title = models.CharField(
        max_length=255,
        verbose_name="course title",
        help_text="format: required, max-255",
        null=False,
        unique=False,
        blank=False,
    )
    slug = models.SlugField(
        max_length=150,
        verbose_name="course safe URL",
        help_text="format: required, letters, numbers, underscore, or hyphens",
        null=False,
        unique=False,
        blank=True,
    )
    short_description = models.TextField(
        verbose_name="Short description",
        help_text="course shot description",
        null=True,
        unique=False,
        blank=True,
    )
    long_description = models.TextField(
        verbose_name="Long description",
        help_text="course long description",
        null=True,
        unique=False,
        blank=True,
    )
    image = models.ImageField(
        upload_to="uploads/",
        default="uploads/default.png",
        verbose_name="product image",
        help_text="format: required, default-default.png",
        unique=False,
        null=False,
        blank=False,
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "course"
        verbose_name_plural = "courses"
        ordering = ["title", "-created_at"]


class Lesson(BaseModel):

    course = models.ForeignKey(
        Course,
        related_name="lessons",
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=255,
        verbose_name="lesson title",
        help_text="format: required, max-255",
        null=False,
        unique=False,
        blank=False,
    )
    slug = models.SlugField(
        max_length=150,
        verbose_name="lesson safe URL",
        help_text="format: required, letters, numbers, underscore, or hyphens",
        null=False,
        unique=False,
        blank=True,
    )
    short_description = models.TextField(
        verbose_name="Short description",
        help_text="lesson shot description",
        null=True,
        unique=False,
        blank=True,
    )
    long_description = models.TextField(
        verbose_name="Long description",
        help_text="lesson long description",
        null=True,
        unique=False,
        blank=True,
    )
    status = models.CharField(
        choices=LessonStatus.choices,
        max_length=1,
        verbose_name="lesson status",
        help_text="format: required, max-1",
        null=False,
        unique=False,
        blank=False,
    )
    lesson_type = models.CharField(
        choices=LessonType.choices,
        max_length=1,
        verbose_name="lesson type",
        help_text="format: required, max-1",
        null=False,
        unique=False,
        blank=False,
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "lesson"
        verbose_name_plural = "lessons"
        ordering = ["title", "-created_at"]


class Comment(BaseModel):
    course = models.ForeignKey(
        Course,
        related_name="comments",
        on_delete=models.CASCADE,
    )
    lesson = models.ForeignKey(
        Lesson, related_name="comments", on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=255,
        verbose_name="comment name",
        help_text="format: required, max-255",
        null=False,
        unique=False,
        blank=False,
    )
    content = models.TextField()
    created_by = models.ForeignKey(
        User, related_name="comments", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "comment"
        verbose_name_plural = "comments"
        ordering = ["name", "-created_at"]
