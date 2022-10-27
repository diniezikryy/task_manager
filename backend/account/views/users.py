from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status, generics

from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ..serializers import AuthenticatedUserSerializer, PublicUserSerializer, TaskSerializer, SubtaskSerializer, ColumnSerializer, BoardSerializer
from ..models import Task, Subtask, Column, Board

class UserBoards(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BoardSerializer

    def get_queryset(self):
        user = self.request.user
        return Board.objects.filter(userId=user)

class SelectedUserBoard(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BoardSerializer

    def get_queryset(self):
        user = self.request.user
        board = Board.objects.filter(id=self.kwargs['pk'])
        return board