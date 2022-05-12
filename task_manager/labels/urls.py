from django.urls import path
from .views import LabelList, CreateLabel, ChangeLabel, Deletelabel

app_name = 'labels'
urlpatterns = [
    path('', LabelList.as_view(), name='list'),
    path('create/', CreateLabel.as_view(), name='create'),
    path('<int:pk>/update/', ChangeLabel.as_view(), name='change'),
    path('<int:pk>/delete/', Deletelabel.as_view(), name='delete'),
]
