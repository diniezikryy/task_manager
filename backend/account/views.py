from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .serializers import AuthenticatedUserSerializer, PublicUserSerializer, TaskSerializer, SubtaskSerializer, ColumnSerializer, BoardSerializer
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

class LoadUsersView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        isAuthenticated = request.user.is_authenticated
        users = User.objects.all()

        try:
            if isAuthenticated:
                serializer = AuthenticatedUserSerializer(users, many=True)
                return Response(
                {"users": serializer.data},
                status=status.HTTP_200_OK
            )
            else:
                serializer = PublicUserSerializer(users, many=True)
                return Response(
                {"users": serializer.data},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Something went wrong when trying to load users'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class LoadUserDetailView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, pk, format=None):
        isAuthenticated = request.user.is_authenticated
        user = User.objects.get(pk=pk)

        try:
            if isAuthenticated:
                serializer = AuthenticatedUserSerializer(user)
                return Response(
                {"user": serializer.data},
                status=status.HTTP_200_OK
            )
            else:
                serializer = PublicUserSerializer(user)
                return Response(
                {"user": serializer.data},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Something went wrong when trying to load users'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class LoadUserView(APIView):
    def get(self, request, format=None):
        try:
            username = request.user
            user = User.objects.get(username=username)
            serializer = AuthenticatedUserSerializer(user)

            return Response(
                {'user': serializer.data},
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
            print(serializer.data)
            
            return Response(
                {'subtask': serializer.data},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Something went wrong when trying to load task detail'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    
    def put(self, request, pk, *args, **kwargs):
        try:
            subtask_object = Subtask.objects.get(pk=pk)

            data = request.data

            subtask_object.title = data["title"]
            subtask_object.isCompleted = data["isCompleted"]

            subtask_object.save()

            return Response(
                {'success': 'Subtask is updated!'},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Something went wrong when trying to update subtask!'},
                status = status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, request, pk, format=None):
        try:
            subtask_object = Subtask.objects.get(pk=pk)
            subtask_object.delete()

            return Response(
                {'success': 'Subtask is deleted'},
                status = status.HTTP_204_NO_CONTENT
            )
        except:
            return Response(
                {'error': 'Something went wrong when trying to delete subtask!'},
                status = status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        


class TaskListView(APIView):
    def get(self, request, format=None):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)

        return Response(
                {'tasks': serializer.data},
                status=status.HTTP_200_OK
            )

    def post(self, request):
        try:
            data = request.data

            task = Task(
                title = data["title"],
                description = data["description"],
                isCompleted = data["isCompleted"],
                userId = User.objects.get(id=data["userId"]),
                column = Column.objects.get(id=data["column"])
            )

            task.save()
            
            return Response(
                {"success": "Successfully added new task!"}
                )
        except:
            return Response(
            {"error": "Something went wrong when trying to add task!"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
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

    def put(self, request, pk, *args, **kwargs):
        try:
            task_object = Task.objects.get(pk=pk)

            data = request.data

            task_object.title = data["title"]
            task_object.description = data["description"]
            task_object.isCompleted = data["isCompleted"]
            task_object.column = Column.objects.get(id=data["column"])

            task_object.save()

            return Response(
                {'success': 'Task is updated!'},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Something went wrong when trying to update task!'},
                status = status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, request, pk, format=None):
        try:
            task_object = Task.objects.get(pk=pk)
            task_object.delete()

            return Response(
                {'success': 'Task is deleted'},
                status = status.HTTP_204_NO_CONTENT
            )
        except:
            return Response(
                {'error': 'Something went wrong when trying to delete task!'},
                status = status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class ColumnListView(APIView):
    def get(self, request, format=None):
        columns = Column.objects.all()
        serializer = ColumnSerializer(columns, many=True)

        return Response(
            {"columns": serializer.data},
            status=status.HTTP_200_OK
        )

    def post(self, request):
        try:
            data = request.data

            # Creating new column object
            new_column = Column(
                name = data["name"],
                userId = User.objects.get(id=data["userId"]),
                board = Board.objects.get(id=data["board"])
            )

            new_column.save()
            
            return Response(
                {"success": "Successfully added new column!"},
                status=status.HTTP_201_CREATED
                )
        except:
            return Response(
            {"error": "Something went wrong when trying to add column!"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
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

    def put(self, request, pk, *args, **kwargs):
        try:
            column_object = Column.objects.get(pk=pk)

            data = request.data

            column_object.name = data["name"]

            column_object.save()

            return Response(
                {'success': 'Column is updated!'},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Something went wrong when trying to update column!'},
                status = status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, request, pk, format=None):
        try:
            column_object = Column.objects.get(pk=pk)
            column_object.delete()

            return Response(
                {'success': 'Column is deleted'},
                status = status.HTTP_204_NO_CONTENT
            )
        except:
            return Response(
                {'error': 'Something went wrong when trying to delete column!'},
                status = status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        

class BoardListView(APIView):
    def get(self, request, format=None):
        boards = Board.objects.all()
        serializer = BoardSerializer(boards, many=True)

        return Response(
            {"boards": serializer.data},
            status=status.HTTP_200_OK
        )

    def post(self, request):
        try:
            data = request.data

            new_board = Board(
                name = data["name"],
                userId = User.objects.get(id=data["userId"])
            )

            new_board.save()
            
            return Response(
                {"success": "Successfully added new board!"},
                status=status.HTTP_201_CREATED
                )
        except:
            return Response(
            {"error": "Something went wrong when trying to add board!"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
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

    def put(self, request, pk, *args, **kwargs):
        try:
            board_object = Board.objects.get(pk=pk)

            data = request.data

            board_object.name = data["name"]

            board_object.save()

            return Response(
                {'success': 'Board is updated!'},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Something went wrong when trying to update board!'},
                status = status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, request, pk, format=None):
        try:
            board_object = Board.objects.get(pk=pk)
            board_object.delete()

            return Response(
                {'success': 'Board is deleted'},
                status = status.HTTP_204_NO_CONTENT
            )
        except:
            return Response(
                {'error': 'Something went wrong when trying to delete board!'},
                status = status.HTTP_500_INTERNAL_SERVER_ERROR
            )


      