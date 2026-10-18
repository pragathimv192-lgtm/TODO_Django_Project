
from django.urls import path,include

from . import views

urlpatterns = [
    # TO DO


    # to add the task
    path('addtask/',views.addTask, name='addtask'),

    # to markasdone
    path('mark_as_done/<int:pk>/',views.mark_as_done, name='mark_as_done'),

    # Edit feature
    path('edit_task/<int:pk>/',views.edit_task,name='edit_task'),

    # to mark as undone
    path('mark_undone/<int:pk>/',views.mark_as_undone,name='mark_as_undone'),

    # to delete task
    path('delete_task/<int:pk>/',views.delete_task,name='delete_task'),
]