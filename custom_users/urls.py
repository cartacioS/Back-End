from django.urls import path
from .views import *

urlpatterns = [
        path('fetch/all', UserListView.as_view(), name='list'),
        path('create', UserCreationView.as_view(), name='create'),
]
