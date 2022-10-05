from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .serializers import UserSerializer, TaskSerializer, SubtaskSerializer, ColumnSerializer, BoardSerializer
from .models import Task, Subtask, Column, Board


class RegisterView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        try:
            data = request.data

            first_name = data['first_name']
            last_name = data['last_name']
            username = data['username']
            password = data['password']
            re_password = data['re_password']

            if password == re_password:
                if len(password) >= 8:
                    if not User.objects.filter(username=username).exists():
                        user = User.objects.create_user(
                            first_name=first_name,
                            last_name=last_name,
                            username=username,
                            password=password,
                        )

                        user.save()

                        if User.objects.filter(username=username).exists():
                            return Response(
                                {'success': 'Account created successfully'},
                                status=status.HTTP_201_CREATED
                            )
                        else:
                            return Response(
                                {'error': 'Something went wrong when trying to create account'},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR
                            )
                    else:
                        return Response(
                            {'error': 'Username already exists'},
                            status=status.HTTP_400_BAD_REQUEST
                        )
                else:
                    return Response(
                        {'error': 'Password must be at least 8 characters in length'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                return Response(
                    {'error': 'Passwords do not match'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except:
            return Response(
                {'error': 'Something went wrong when trying to register account'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class LoadUserView(APIView):
    def get(self, request, format=None):
        try:
            user = request.user
            user = UserSerializer(user)

            return Response(
                {'user': user.data},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Something went wrong when trying to load user'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class SubtaskListView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        subtasks = Subtask.objects.all()
        serializer = SubtaskSerializer(subtasks, many=True)
        return Response(
            {"subtasks": serializer.data},
            status=status.HTTP_200_OK
        )

    def post(self, request):
        print(request.data)
        serializer = SubtaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"success": "Successfully added new subtask!"}
                )
        else:
            return Response(
            {"error": "Something went wrong when trying to add subtask!"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        

            

class SubtaskDetailView(APIView):
    def get(self, request, pk, format=None):
        try:
            subtask = Subtask.objects.get(pk=pk)
            serializer = SubtaskSerializer(subtask)
            return Response(
                {'subtask': serializer.data},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Something went wrong when trying to load task detail'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class TaskListView(APIView):
    def get(self, request, format=None):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(
                {'tasks': serializer.data},
                status=status.HTTP_200_OK
            )

class TaskDetailView(APIView):
    def get(self, request, pk, format=None):
        try:
            task = Task.objects.get(pk=pk)
            serializer = TaskSerializer(task)
            return Response(
                {'task': serializer.data},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Something went wrong when trying to load task detail'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class ColumnListView(APIView):
    def get(self, request, format=None):
        columns = Column.objects.all()
        serializer = ColumnSerializer(columns, many=True)
        return Response(
            {"columns": serializer.data},
            status=status.HTTP_200_OK
        )

class ColumnDetailView(APIView):
    def get(self, request, pk, format=None):
        try:
            column = Column.objects.get(pk=pk)
            serializer = ColumnSerializer(column)
            return Response(
                {'column': serializer.data},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Something went wrong when trying to load task detail'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class BoardListView(APIView):
    def get(self, request, format=None):
        boards = Board.objects.all()
        serializer = BoardSerializer(boards, many=True)
        return Response(
            {"boards": serializer.data},
            status=status.HTTP_200_OK
        )

class BoardDetailView(APIView):
    def get(self, request, pk, format=None):
        try:
            board = Board.objects.get(pk=pk)
            serializer = BoardSerializer(board)
            return Response(
                {'board': serializer.data},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Something went wrong when trying to load task detail'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


      