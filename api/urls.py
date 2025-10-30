from django.urls import path
from .views import *

urlpatterns = [
    path('',apiOverview,name='api_view'),
    path('create/',createTodo,name='create_todo'),
    path('all/',getTodos,name='get_todo'),
    path('get/<int:pk>',getSingleTodo,name='get_single_todo'),
    path('update/<int:pk>',updateTodo,name='update_todo'),
    path('delete/<int:pk>',deleteTodo,name='delete_todo'),
]