from django.contrib import admin
from .models import Course, CourseModule, CourseContent, CourseComment

# Register your models here.

# admin.site.register(Course)
# admin.site.register(CourseContent)
# admin.site.register(CourseComment)


class ContentInline(admin.StackedInline):
    model = CourseContent
    extra = 0


class ModuleInline(admin.StackedInline):
    model = CourseModule
    extra = 0
    inlines = [ContentInline]


class CommentInline(admin.StackedInline):
    model = CourseComment
    extra = 0


@admin.register(CourseModule)
class ModuleAdmin(admin.ModelAdmin):
    inlines = [ContentInline]  # Include CourseContentInline in the ModuleAdmin

    list_display = ("title", "course")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [ModuleInline, CommentInline]

    list_display = ("title",)
