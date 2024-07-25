from django.contrib import admin
from .models import StudentLocation, TeacherFinancialOverview

# Register your models here.

class ContentInline(admin.StackedInline):
    model = StudentLocation
    extra = 0
    

@admin.register(TeacherFinancialOverview)
class ModuleAdmin(admin.ModelAdmin):
    inlines = [ContentInline]  # Include CourseContentInline in the ModuleAdmin

    # list_display = ("title", "course")
