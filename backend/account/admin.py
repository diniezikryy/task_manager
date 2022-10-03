from django.contrib import admin
from .models import Task, Subtask, Column, Board
# Register your models here.

admin.site.register(Task)
admin.site.register(Subtask)
admin.site.register(Column)
admin.site.register(Board)