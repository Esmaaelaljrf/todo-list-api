from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import BasePermission, IsAuthenticated
from .models import Tasks
from .serializers import TaskSerializer, UserCreating

# Create your views here.

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class UserCreatingView(APIView):
    #WE use APIView because we will send and return Json data
    #we didnt use ListCreateAPIView becuse we have a deffrince logic and serzilaes for it.
    def post(self, request):
        serializer = UserCreating(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User registered successfully."},
                status=status.HTTP_201_CREATED
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskListCreateView(ListCreateAPIView):
    """
    To Get and Post Task
    """
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

class TaskUpdateDeleteview(RetrieveUpdateDestroyAPIView):
        """
        To Update and Delete and Get Task
        """
        permission_classes =[IsAuthenticated, IsOwner]
        queryset = Tasks.objects.all()
        serializer_class = TaskSerializer

