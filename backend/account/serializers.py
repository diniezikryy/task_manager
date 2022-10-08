from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task, Subtask, Column, Board


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'id')

class SubtaskSerializer(serializers.ModelSerializer):
    userId = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=False)

    class Meta:
        model = Subtask
        fields = (
            'id',
            'title',
            'isCompleted',
            'taskId',
            'userId',
        )

class TaskSerializer(serializers.ModelSerializer):
    userId = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=False)
    subtasks = SubtaskSerializer(many=True)
    column = serializers.PrimaryKeyRelatedField(queryset=Column.objects.all(), many=False)

    class Meta:
        model = Task
        fields = '__all__'

class ColumnSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Column
        fields = '__all__'

class BoardSerializer(serializers.ModelSerializer):
    columns = ColumnSerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields = '__all__'



