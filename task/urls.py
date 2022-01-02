from django.urls import path
from .views import TaskList

app_name = 'tasks'

urlpatterns = [
    path('list/', TaskList.as_view(), name='list'),
]
