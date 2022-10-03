from django.urls import path
from .views import RegisterView, LoadUserView, TaskListView, SubtaskListView,TaskDetailView, ColumnListView, SubtaskDetailView, ColumnDetailView, BoardListView, BoardDetailView


urlpatterns = [
    path('register', RegisterView.as_view()),
    path('user', LoadUserView.as_view()),
    path('subtasks', SubtaskListView.as_view()),
    path('subtasks/<int:pk>', SubtaskDetailView.as_view()),
    path('tasks', TaskListView.as_view()),
    path('tasks/<int:pk>', TaskDetailView.as_view()),
    path('columns', ColumnListView.as_view()),
    path('columns/<int:pk>', ColumnDetailView.as_view()),
    path('boards', BoardListView.as_view()),
    path('boards/<int:pk>', BoardDetailView.as_view()),
]
