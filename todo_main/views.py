from django.http import HttpResponse
from django.shortcuts import render

from todo.models import Task

def home(request):
    # uncompleted task
    tasks=Task.objects.filter(is_completed=False).order_by('-created_at')
    # print(tasks)

    #completed task
    completed_task=Task.objects.filter(is_completed=True)

    context={
        'tasks':tasks,
        'completed_task':completed_task
    }
    return render(request,'home.html',context) 