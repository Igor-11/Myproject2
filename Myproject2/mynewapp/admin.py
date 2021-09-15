from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'description', 'creation_date', 'is_completed', 'priority']

admin.site.register(Task, TaskAdmin)