from django.urls import path
from . import views

urlpatterns = [
    path('tasks-list', views.get_all_tasks, name ='tasks_list'),
    path('new-task', views.create_new_task_form, name = 'new_task_form'),
    path('save-new-task', views.save_new_task, name = 'save_new_task'),
    path('delete-task/<int:pk>', views.delete_task, name='delete_task'),
    path('view-task/<int:pk>', views.view_task, name='view_task'),
    path('edit-task/<int:pk>', views.edit_task_form, name='edit_task_form'),
    path('copy-task/<int:pk>', views.copy_task, name='copy_task'),
    path('finish-task/<int:pk>', views.finish_task, name='finish_task'),

]