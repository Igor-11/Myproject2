from django.db import models
from django.db.models.fields import DateTimeField
from .constants import priorities

class Task(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=200, choices=priorities.PRIORITY_TYPES)
    copy_from = models.ForeignKey('self',null=True, on_delete=models.CASCADE)