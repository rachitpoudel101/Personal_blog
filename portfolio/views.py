from django.shortcuts import render
from .models import Projects

def home (request):
    projects = Projects.objects.all()
    return render(request,'HTML/home.html',{'projects':projects})