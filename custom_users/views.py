from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import UserSerializer
from .models import User

class UserListView(generics.GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self, request):
        users = self.get_queryset()
        serialized = UserSerializer(users, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

class UserCreationView(generics.GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        u = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
