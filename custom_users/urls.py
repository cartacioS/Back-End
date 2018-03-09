from django.urls import path
from .views import *

urlpatterns = [
        path('fetch/all', UserListView.as_view(), name='list'),
        path('login', UserLoginView.as_view(), name='login'),
        path('create', UserCreationView.as_view(), name='create'),
]
