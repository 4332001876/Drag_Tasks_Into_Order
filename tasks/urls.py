from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('<int:pk>/update/', views.task_update, name='task_update'),
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('<int:pk>/toggle-complete/', views.task_toggle_complete, name='task_toggle_complete'),
    path('update-order/', views.update_task_order, name='update_task_order'),
] 