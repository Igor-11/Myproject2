from .models import Task

def delete_completed_tasks():
    Task.objects.filter(is_completed=True).delete()