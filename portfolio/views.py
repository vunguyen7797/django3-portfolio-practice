from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all() # get all objects with Project model
    return render(request, 'portfolio/home.html', {'projects': projects})
