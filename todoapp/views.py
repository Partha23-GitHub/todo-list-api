from django.shortcuts import render
# rest_framework imports
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

#models & serializers import
from .models import TODO
from .serializers import TODOSerializer


class ToDoView(generics.ListCreateAPIView):    #for viewing & Creating todo contents
    permission_classes = [IsAuthenticated]
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer

class ToDodescView(generics.RetrieveUpdateDestroyAPIView): # for individual viewing & Updating and deleting
    permission_classes = [IsAuthenticated]
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer
    