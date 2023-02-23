from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Project
from .forms import ProjectForm
# Create your views here.


def main(response):
    projects = Project.objects.all()
    return render(response,"main/main.html",{"projects":projects})

def project(response,pk):
    project = Project.objects.get(id=pk)
    reviews = project.review_set.all()
    context = {"project": project, "reviews": reviews}
    print("Project: ", project)
    return render(response, 'main/single-project.html', context)

def create(response):
    form = ProjectForm()

    if response.method == 'POST':
        print("Data from form: ", response.POST["Title"])

    context = {"form": form}
    return render(response, 'main/create.html', context)