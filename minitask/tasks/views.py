from django.shortcuts import render
from .models import Task

from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Task, UserProfile
from .forms import TaskForm


def home_view(request):
  
  taches = Task.objects.all()


  context = {
      'taches': taches,
  }

  
  return render(request, 'tasks/home.html', context)






def home_view(request):
    taches = Task.objects.all()
    context = {
        'taches': taches,
    }
    return render(request, 'tasks/home.html', context)


@login_required
def add_task_view(request):
    """
    Vue pour ajouter une tâche et l'associer au profil de l'utilisateur connecté.
    """
    # Récupère ou gère le UserProfile lié à l'utilisateur connecté
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            # On n'enregistre pas tout de suite en base pour pouvoir modifier l'instance
            task = form.save(commit=False)
            # Association automatique du profil
            task.profil = user_profile
            task.save()
            return redirect('home')  # Redirige vers la page d'accueil après l'ajout
    else:
        form = TaskForm()

    context = {
        'form': form,
    }
    return render(request, 'tasks/add_task.html', context)