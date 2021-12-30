from commons.utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.dispatch import receiver

from course.models import Category, Course, Lesson


@receiver(pre_save, sender=Category)
def pre_save_category_slug_generator(sender, instance, *args, **kwargs):
    print("Fora do If")
    if not instance.slug:
        print("dentro do if")
        instance.slug = unique_slug_generator(sender, instance)


@receiver(pre_save, sender=Course)
def pre_save_course_slug_generator(sender, instance, *args, **kwargs):

    if not instance.slug:
        instance.slug = unique_slug_generator(sender, instance)


@receiver(pre_save, sender=Lesson)
def pre_save_lesson_slug_generator(sender, instance, *args, **kwargs):

    if not instance.slug:
        instance.slug = unique_slug_generator(sender, instance)
