import random
import string

from django.utils.text import slugify


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
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
