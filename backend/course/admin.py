from django.contrib import admin
from .models import Course, CourseContent, CourseComment

# Register your models here.

# admin.site.register(Course)
# admin.site.register(CourseContent)
# admin.site.register(CourseComment)

class ContentInline(admin.StackedInline):
    model = CourseContent
    extra = 0

class CommentInline(admin.StackedInline):
    model = CourseComment
    extra = 0

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [ContentInline, CommentInline]

    list_display = ('title',)