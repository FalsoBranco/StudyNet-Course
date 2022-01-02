from accounts.models import CustomUser as User
from course.models import Comment, Course, Lesson


def comment_create(
    *,
    name: str,
    content: str,
    user: User,
    lesson: Lesson,
    course: Course,
) -> Comment:

    obj: Comment = Comment.objects.create(
        name=name,
        content=content,
        created_by=user,
        course=course,
        lesson=lesson,
    )
    obj.full_clean()
    obj.save()
    return obj
