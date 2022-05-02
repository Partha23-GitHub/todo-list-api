from django.shortcuts import render
# rest_framework imports
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

#models & serializers import
from .models import TODO
from .serializers import TODOSerializer
from todoapp import serializers


class ToDoView(generics.ListCreateAPIView):    #for viewing & adding todo contents
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer

class ToDodescView(generics.RetrieveUpdateDestroyAPIView): # for individual viewing & Updating and deleting
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer
    