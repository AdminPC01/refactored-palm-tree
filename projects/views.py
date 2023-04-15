from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.http import HttpRequest
from .models import Project
from .forms import ProjectForm
# Create your views here.


def main(response):
    projects = Project.objects.all()
    return render(response,"main.html",{"projects":projects})

def project(response,pk):
    project = Project.objects.get(id=pk)
    reviews = project.review_set.all()
    context = {"project": project, "reviews": reviews}
    print("Project: ", project)
    obj = HttpRequest
    return render(response, "projects/single-project.html", context)

def create(response):
    form = ProjectForm()

    if response.method == 'POST':
        form = ProjectForm(response.POST, response.FILES)
        if (form.is_valid):
           form.save()
        return redirect("projects")
    context = {"form": form}
    return render(response, "projects/create.html", context)

# def update(response):
#     form = ProjectForm()
#
#     if response.method == "POST":
#         form = ProjectForm(response.POST["Title"])
#         for
#

def update_project(response,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if response.method == "POST":
        form = ProjectForm(response.POST, response.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect("projects")
    context = {"form":form}
    return render(response, "projects/create.html",context)

def delete(response,pk):
    project = Project.objects.get(id=pk)
    if response.method == 'POST':
        project.delete()
        return redirect("projects")
    return render(response,"projects/delete.html",{"project":project})