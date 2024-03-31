from django.db import models
from django.core.validators import (
    FileExtensionValidator,
    MinValueValidator,
    MaxValueValidator,
)

from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

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

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #
    #     # After saving the course, update is_instructor for all associated instructors
    #     for instructor in self.instructors.all():
    #         if not instructor.is_instructor:
    #             instructor.is_instructor = True
    #             instructor.save()

    # def save(self, *args, **kwargs):
    #     course = super(Course, self).save(*args, **kwargs)
    #     print("=------------------------------=")
    #     print("pk: ", self.pk)
    #     print("title: ", self.title)
    #     print("All Instructors: ", self.instructors.all())
    #     print("")
    #     for instructor in self.instructors.all():
    #         if instructor.is_instructor:
    #             continue
    #         instructor.is_instructor = True
    #         instructor.save()
    #         print(instructor, instructor.is_instructor)
    #
    #     print("=------------------------------=")


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


class CourseContent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

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

    # def track_progress(self, student):
    #     try:
    #         progress = ContentProgress.objects.get(student=student, content=self)
    #         return progress.progress
    #     except ContentProgress.DoesNotExist:
    #         return "not_started"

    def __str__(self):
        return f"{self.title}"
