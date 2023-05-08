from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.http import HttpRequest
from .models import Project
from users.models import Profile
from django.contrib.auth.decorators import login_required
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
    return render(response, "projects/single-project.html", context)


@login_required(login_url="login")
def create(response):
    profile = response.user.profile
    # owner = response.project.owner

    form = ProjectForm()

    if response.method == 'POST':
        form = ProjectForm(response.POST, response.FILES)
        if (form.is_valid):
           project = form.save(commit=False)
           project.owner = profile
           project.save()
        return redirect('account')
    context = {"form": form}
    return render(response, "projects/create.html", context)


@login_required(login_url="login")
def update_project(response,pk):
    profile = response.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if response.method == "POST":
        form = ProjectForm(response.POST, response.FILES, instance=project)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect("account")
    context = {"form":form}
    return render(response, "projects/create.html",context)


@login_required(login_url="login")
def delete(response,pk):
    profile = response.user.profile
    project = profile.project_set.get(id=pk)
    context = {"object": project}
    if response.method == 'POST':
        project.delete()
        return redirect("account")
    return render(response,"delete-template.html",{"object":project})


