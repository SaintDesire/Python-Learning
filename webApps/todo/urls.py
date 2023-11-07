from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo, name='todo'),
    path('<int:pk>/update_todo_status', views.update_todo_status, name='update_todo_status'),
    path('<int:pk>/edit', views.editTodo, name='editTodo'),
    path('<int:pk>/delete', views.deleteTodo, name='deleteTodo'),
]
