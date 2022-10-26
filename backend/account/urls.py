from django.urls import path
from .views import RegisterView, LoadUserView, LoadUsersView, LoadUserDetailView, TaskListView, SubtaskListView,TaskDetailView, ColumnListView, SubtaskDetailView, ColumnDetailView, BoardListView, BoardDetailView, UserBoards


urlpatterns = [
    path('register', RegisterView.as_view()),
    path('user', LoadUserView.as_view()),
    path('users/<str:username>', LoadUserDetailView.as_view()),
    path('users', LoadUsersView.as_view()),
    path('subtasks', SubtaskListView.as_view()),
    path('subtasks/<int:pk>', SubtaskDetailView.as_view()),
    path('tasks', TaskListView.as_view()),
    path('tasks/<int:pk>', TaskDetailView.as_view()),
    path('columns', ColumnListView.as_view()),
    path('columns/<int:pk>', ColumnDetailView.as_view()),
    path('boards', BoardListView.as_view()),
    path('boards/<int:pk>', BoardDetailView.as_view()),
    path('boards/<int:pk>', BoardDetailView.as_view()),
    path('user/boards', UserBoards.as_view()),
]


