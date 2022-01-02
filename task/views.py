from django.shortcuts import render
from django.views.generic import ListView

from .models import Task

# Create your views here.


class TaskList(ListView):
    template_name = 'tasks/list.html'
    context_object_name = 'tasks'
    model = Task
