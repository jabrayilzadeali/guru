from django.contrib import admin
from .models import Course, CourseContent, CourseComment

# Register your models here.

admin.site.register(Course)
admin.site.register(CourseContent)
admin.site.register(CourseComment)
