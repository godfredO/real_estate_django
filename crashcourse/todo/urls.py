from django.urls import path
from . import views

app_name='todos'

urlpatterns = [
    path('',  views.todo_list),
    path('<int:id>/', views.todo_detail),
    path('create/', views.todo_create),
    path('<int:id>/update/', views.todo_update),
    path('<int:id>/delete/', views.todo_delete),
    ]