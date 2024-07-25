from django.db import models
from django.core.validators import (
    FileExtensionValidator,
    MinValueValidator,
    MaxValueValidator,
)

from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
# from django.db.models.signals import pre_save
# from django.dispatch import receiver

# from student.models import Student
# from student.models import Purchase

# Create your models here.
User = get_user_model()


def course_thumbnail(instance, filename):
    return f"course-assets/{instance.title}/thumbnail/{filename}"


def course_trailer(instance, filename):
    return f"course-assets/{instance.title}/videos/{filename}"


def course_content_thumbnail(instance, filename):
    return (
        f"course-assets/{instance.course.title}/thumbnail/{instance.title}/{filename}"
    )


def course_content_videos(instance, filename):
    return f"course-assets/{instance.course.title}/videos/{instance.title}/{filename}"


class Course(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    instructors = models.ManyToManyField(User)

    img = models.ImageField(upload_to=course_thumbnail, blank=True, null=True)
    video = models.FileField(
        upload_to=course_trailer,
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=["MOV", "avi", "mp4", "webm", "mkv"]
            )
        ],
    )

    price = models.DecimalField(max_digits=10, decimal_places=2)
    view_count = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} | {self.price}"


class CourseModule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # order = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=256)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.course.title}"

    # def save(self, *args, **kwargs):
    #     if not self.order:
    #         # Generate order based on the existing modules
    #         max_order = CourseModule.objects.filter(course=self.course).aggregate(
    #             max_order=models.Max("order")
    #         )["max_order"]
    #         self.order = max_order + 1 if max_order is not None else 1
    #     super().save(*args, **kwargs)


class CourseContent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # course = models.ForeignKey(Course, on_delete=models.CASCADE)
    module = models.ForeignKey(CourseModule, on_delete=models.CASCADE)

    title = models.CharField(max_length=256)

    img = models.ImageField(upload_to=course_content_thumbnail, blank=True, null=True)
    video = models.FileField(
        upload_to=course_content_videos,
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=["MOV", "avi", "mp4", "webm", "mkv"]
            )
        ],
    )
    content = RichTextField()

    is_free = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"


class CourseComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)]
    )
    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.course.title}"
