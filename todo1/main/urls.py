from django.urls import path

from main.views import *

urlpatterns = [
    path('<int:pk>/', todo_tasks),
    path('<int:pk>/completed/', completed_tasks)
]