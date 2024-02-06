from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class CourseComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)

    rating = models.FloatField()
    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.course.title}"


class CourseContent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)

    title = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)

    content_type = models.CharField(max_length=10, choices=[('text', 'Text'), ('video', 'Video')])
    content = models.TextField()
    
    is_free = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Content by {self.user.username} on {self.course.title}"
    

class ContentProgress(models.Model):
    student = models.ForeignKey("Student", on_delete=models.CASCADE)
    content = models.ForeignKey("CourseContent", on_delete=models.CASCADE)
    progress = models.CharField(max_length=11, choices=[('not_started', 'not started'), ('started', 'Started'), ('finished', 'Finished')])
    
    def __str__(self):
        return f"Content Progress {self.progress}"


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)

    def __str__(self):
        return f"Student {self.user}"
    
    
    


class Course(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    instructors = models.ManyToManyField(User)
    
    price = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} on {self.price}"