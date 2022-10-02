from django.urls import path
from .views import RegisterView, LoadUserView, TaskListView, SubtaskListView,TaskDetailView


urlpatterns = [
    path('register', RegisterView.as_view()),
    path('user', LoadUserView.as_view()),
    path('tasks', TaskListView.as_view()),
    path('tasks/<int:pk>', TaskDetailView.as_view()),
    path('subtasks', SubtaskListView.as_view()),
]
