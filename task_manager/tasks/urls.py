from django.urls import path
from .views import (
    TaskList,
    TaskView,
    CreateTask,
    ChangeTask,
    DeleteTask,
)

app_name = 'tasks'
urlpatterns = [
    path('', TaskList.as_view(), name='list'),
    path('create/', CreateTask.as_view(), name='create'),
    path('<int:pk>/update/', ChangeTask.as_view(), name='change'),
    path('<int:pk>/delete/', DeleteTask.as_view(), name='delete'),
    path('<int:pk>/', TaskView.as_view(), name='viewer'),
]
