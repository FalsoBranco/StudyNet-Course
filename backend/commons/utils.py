import random
import string
from typing import Any, Dict

from django.utils.text import slugify
from rest_framework import serializers


def random_string_generator(
    size: int = 10,
    chars: str = string.ascii_lowercase + string.digits,
) -> str:
    return "".join(random.choice(chars) for _ in range(size))


def unique_slug_generator(sender, instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    max_length = sender._meta.get_field("slug").max_length
    slug = slug[:max_length]
    qs_exists = sender.objects.filter(slug=slug).exists()

    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug[: max_length - 5], randstr=random_string_generator(size=4)
        )

        return unique_slug_generator(sender, instance, new_slug=new_slug)
    return slug


def create_serializer_class(name: str, fields: Dict[str, Any]):
    return type(name, (serializers.Serializer,), fields)


def inline_serializer(*, fields: Dict[str, Any], data=None, **kwargs):
    serializer_class = create_serializer_class(name="", fields=fields)

    if data is not None:
        return serializer_class(data=data, **kwargs)
    return serializer_class(**kwargs)
