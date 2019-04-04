from rest_framework import serializers
from . import models


class TodosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Todos
        fields = ('id','title','completed')