from django.urls import path

from main.views import *

urlpatterns = [
    path('todos/', todo_tasks),
    path('todos/1/completed/', completed_tasks)
]