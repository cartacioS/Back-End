from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import (RequestSerializer)
from .models import UserRequests

# Create your views here.

class RequestListView(generics.GenericAPIView):
    serializer_class = RequestSerializer
    queryset = UserRequests.objects.all()

    def get(self, request):
        requests = self.get_queryset()
        serializer = RequestSerializer(requests, many = True)
        return Response(serialized.data, status=status.HTTP_200_OK)

class RequestCreationView(generics.GenericAPIView):
    serializer_class = RequestSerializer
    queryset = UserRequests.objects.all()

    def post(self, request):
        serializer = RequestSerializer(data=request.data, context = { 'request' : request })
        serializer.is_valid(raise_exception=True)
        u = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
