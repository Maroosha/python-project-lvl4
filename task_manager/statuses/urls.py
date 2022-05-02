from django.urls import path
from .views import StatusesList, CreateStatus, ChangeStatus, DeleteStatus

app_name = 'statuses'
urlpatterns = [
    path('', StatusesList.as_view(), name='list'),
    path('create/', CreateStatus.as_view(), name='create'),
    path('<int:pk>/update/', ChangeStatus.as_view(), name='change'),
    path('<int:pk>/delete/', DeleteStatus.as_view(), name='delete'),
]
