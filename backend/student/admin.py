from django.contrib import admin
from .models import Student, Cart, Purchase, ContentProgress


admin.site.register(Student)
admin.site.register(Cart)
admin.site.register(Purchase)
admin.site.register(ContentProgress)
