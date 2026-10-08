from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
  # Lié au modèle User de Django par une relation OneToOne
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  bio = models.TextField(blank=True, null=True)
  telephone = models.CharField(max_length=20, blank=True, null=True)
  date_naissance = models.DateField(blank=True, null=True)

  def __str__(self):
    return self.user.username


class Task(models.Model):
  STATUT_CHOICES = [
      ('en_cours', 'En cours'),
      ('termine', 'Terminé'),
  ]

  titre = models.CharField(max_length=200)
  description = models.TextField(blank=True, null=True)
  statut = models.CharField(
      max_length=20, choices=STATUT_CHOICES, default='en_cours'
  )
  # Relation ForeignKey vers UserProfile (à qui appartient la tâche)
  profil = models.ForeignKey(
      UserProfile, on_delete=models.CASCADE, related_name='tasks'
  )

  def __str__(self):
    return self.titre