from django.urls import path
from .views import *

urlpatterns = [
        path('fetch/all', RequestListView.as_view(), name='list'),
        path('create', RequestCreationView.as_view(), name='create'),
]
