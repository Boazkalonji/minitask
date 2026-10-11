from django.urls import path
from . import views  

urlpatterns = [
    
    path('', views.home_view, name='home'),
    path('tasks/add/', views.add_task_view, name='add_task'),
]