from django.shortcuts import render
from .models import Task


def home_view(request):
  
  taches = Task.objects.all()


  context = {
      'taches': taches,
  }

  
  return render(request, 'tasks/home.html', context)