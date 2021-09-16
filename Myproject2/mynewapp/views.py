from django.shortcuts import render
from .models import Task
from .constants import priorities
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.forms.models import model_to_dict
from django.db.models import Count

def get_all_tasks(request):
    tasks = Task.objects.annotate(number_of_copies=Count('task'))
    tasks = list(map(lambda task: {**(task.__dict__),'priority':list(filter(lambda priority: priority[0] == task.priority, priorities.PRIORITY_TYPES))[0][1]}, tasks))
    new_tasks = list(filter(lambda task: not task['is_completed'], tasks))
    completed_tasks = list(filter(lambda task: task['is_completed'], tasks))
    context = {'new_tasks' : new_tasks, 'completed_tasks': completed_tasks}
    return render(request, 'mynewapp/task_list.html', context)

def create_new_task_form(request):
    context = {'priority_types' : priorities.PRIORITY_TYPES}
    return render(request, 'mynewapp/create_task_form.html', context)

def save_new_task(request):
    title = request.POST['title']
    subtitle = request.POST['subtitle']
    description = request.POST['description']
    priority = request.POST['priority']
    new_task = Task(title=title, subtitle=subtitle, description=description, priority=priority)
    new_task.save()
    return HttpResponseRedirect(reverse('tasks_list'))

def delete_task(request, pk):
    Task.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('tasks_list'))

def view_task(request, pk):
    task = Task.objects.get(pk=pk)
    context = {'task':task}
    return render(request, 'mynewapp/view_task.html', context)

def edit_task_form(request, pk):
    if request.method == 'POST':
        title = request.POST.get('title')
        subtitle = request.POST.get('subtitle')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        edited_task = Task.objects.get(pk=pk)
        edited_task.title = title
        edited_task.subtitle = subtitle
        edited_task.description = description
        edited_task.priority = priority
        edited_task.save()
        return HttpResponseRedirect(reverse('tasks_list'))
    else:
        task = Task.objects.get(pk=pk)
        context = {'task':task, 'priority_types': priorities.PRIORITY_TYPES}
        return render(request, 'mynewapp/edit_task_form.html', context)

def copy_task(request, pk):
    task = Task.objects.get(pk=pk)
    old_task_id = task.id
    task.id = None
    task.save()
    copied_task = Task.objects.get(pk=task.id)
    copied_task.copy_from = Task.objects.get(pk=old_task_id)
    copied_task.save()
    return HttpResponseRedirect(reverse('tasks_list'))

def finish_task(request,pk):
    task = Task.objects.get(pk=pk)
    task.is_completed = True
    task.save()
    return HttpResponseRedirect(reverse('tasks_list'))



    



