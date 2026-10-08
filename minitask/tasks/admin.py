from django.contrib import admin
from .models import Task, UserProfile

admin.site.register(UserProfile)
admin.site.register(Task)