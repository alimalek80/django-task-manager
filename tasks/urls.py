from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('update/<int:pk>/', views.task_update, name='task_update'),
    path('complete/<int:pk>/', views.task_complete, name='task_complete'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('start/<int:pk>/', views.task_start, name='task_start'),
    path('in_progress/<int:pk>/', views.task_in_progress, name='task_in_progress'),
]