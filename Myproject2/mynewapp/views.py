from django.shortcuts import render
from .models import Task
from .constants import priorities
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.forms.models import model_to_dict

def get_all_tasks(request):
    tasks = Task.objects.all()
    tasks = list(map(lambda task: {**(task.__dict__),'priority':list(filter(lambda priority: priority[0] == task.priority, priorities.PRIORITY_TYPES))[0][1]}, tasks))
    context = {'tasks' : tasks}
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
    task.id = None
    task.save()
    task = Task.objects.get(pk=pk)
    task.copy_from = task
    task.save()
    return HttpResponseRedirect(reverse('tasks_list'))


    



