from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task, Subtask, Column


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'id')

class SubtaskSerializer(serializers.ModelSerializer):
    userId = UserSerializer()

    class Meta:
        model = Subtask
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    userId = UserSerializer()
    subtasks = SubtaskSerializer(many=True)

    class Meta:
        model = Task
        fields = '__all__'

class ColumnSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)

    class Meta:
        model = Column
        fields = ('name', 'tasks')

