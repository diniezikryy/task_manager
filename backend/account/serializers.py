from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task, Subtask, Column, Board


class AuthenticatedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name', 
            'last_name', 
            'username', 
            'id',
        )

class PublicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 
            'id',
        )

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
        fields = (
            'id',
            'title',
            'description',
            'isCompleted',
            'userId',
            'subtasks',
            'column',
        )

class ColumnSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)

    class Meta:
        model = Column
        fields = (
            'id',
            'name',
            'userId',
            'tasks',
            'board',
        )

class BoardSerializer(serializers.ModelSerializer):
    columns = ColumnSerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields = (
            'id',
            'name',
            'userId',
            'columns',
        )



