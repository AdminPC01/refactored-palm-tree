from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Project
# Create your views here.


def view(response):
    projects = Project.objects.all()
    return render(response,"main/main.html",{"projects":projects})
def v2(response,pk):
    project = Project.objects.get(id=pk)
    context = {"projects":project}
    print("Project: ", project)
    return render(response,'main/User.html',context)