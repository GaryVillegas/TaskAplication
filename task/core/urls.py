from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('tasks', task, name='tasks'),
    path("delete-tasks/", delete_tasks, name="delete_tasks")
]