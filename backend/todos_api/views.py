from django.shortcuts import render
from rest_framework import viewsets

from . import models
from . import serializers

# Create your views here.
class TodosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TodosSerializer
    queryset = models.Todos.objects.all()