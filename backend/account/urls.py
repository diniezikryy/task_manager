from django.urls import path
from .views import RegisterView, LoadUserView, TaskListView


urlpatterns = [
    path('register', RegisterView.as_view()),
    path('user', LoadUserView.as_view()),
    path('tasks', TaskListView.as_view()),
]
