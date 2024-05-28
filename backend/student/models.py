from django.db import models
from django.contrib.auth import get_user_model
from course.models import Course, CourseContent
from decimal import Decimal

# Create your models here.
User = get_user_model()


class Student(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def increase_balance(self, amount):
        if not isinstance(amount, Decimal):
            amount = Decimal(amount)
        self.balance += amount
        self.save()

    def __str__(self):
        return f"{self.user}"


class Cart(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("student", "course")

    def __str__(self):
        return f"{self.student} - {self.course}"


class Purchase(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("student", "course")

    def save(self, *args, **kwargs):
        if self.student.balance >= self.course.price:
            self.student.balance -= self.course.price
            self.student.save()
            super().save(*args, **kwargs)
        else:
            raise ValueError("Insufficient balance")

    def __str__(self):
        return f"{self.student} | {self.course}"


class ContentProgress(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    content = models.ForeignKey(CourseContent, on_delete=models.CASCADE)
    progress = models.CharField(
        max_length=11,
        choices=[
            ("not_started", "not started"),
            ("started", "Started"),
            ("finished", "Finished"),
        ],
    )

    class Meta:
        unique_together = ("student", "content")

    def save(self, *args, **kwargs):
        if Purchase.objects.filter(
            student=self.student, course=self.content.course
        ).exists():
            self.student.save()
            super().save(*args, **kwargs)
        else:
            raise ValueError("Student doesn't own this course")

    def __str__(self):
        return f"Progress: {self.student.user} - {self.content.course.title} - {self.content.title} - {self.progress}"
