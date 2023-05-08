
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from .forms import CustomUserCreationForm, ProfileForm,SkillForm
from .utils import searchProfiles
# Create your views here.


def loginUser(response):
    page = "login"

    if response.user.is_authenticated:
        return redirect("profiles")
    if response.method == "POST":
        username = response.POST["username"]
        password = response.POST["password"]
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(response,"Invalid username")
        user = authenticate(response, username=username, password=password)

        if user is not None:
            login(response,user)
            messages.error(response,"User was successfully logged in")
            return redirect("profiles")
        else:
            messages.error(response,"Username or password is incorrect")

    return render(response,"users/login-register.html",{"page":page})


def logoutUser(response):
    logout(response)
    messages.info(response,"User was logged out")
    return redirect('login')

def registerUser(response):
    page = "register"
    form = CustomUserCreationForm()
    if response.method == "POST":
        form = CustomUserCreationForm(response.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(response,"User was successfully registered")
            login(response,user)
            return redirect("profiles")
        else:
            messages.error(response,"An error have occured")

    context = {"page": page,"form":form}
    return render(response,"users/login-register.html",context)


def profiles(response):

    profiles, search_query = searchProfiles(response)

    context = {"profiles": profiles,"search_query":search_query}
    return render(response,"users/profiles.html",context)

def userProfile(response,pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    context = {"profile":profile,"topSkills":topSkills,"otherSkills":otherSkills}
    return render(response,"users/user-profile.html", context)


@login_required(login_url="login")
def userAccount(response):
    profile = response.user.profile
    projects = profile.project_set.all()
    skills = profile.skill_set.all()
    context = {"profile":profile,"projects":projects,"skills":skills}
    return render(response,"users/account.html",context)

@login_required(login_url="login")
def editAccount(response):
    profile = response.user.profile
    form = ProfileForm(instance=profile)
    if response.method == "POST":
        form = ProfileForm(response.POST, response.FILES,instance=profile)
        if form.is_valid():
            form.save()
            redirect("account")
    context = {"form":form}
    return render(response,"users/profile-form.html", context)

@login_required(login_url="create-skill")
def createSkill(response):
    profile = response.user.profile
    form = SkillForm()

    if response.method == "POST":
        form = SkillForm(response.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(response,"The skill was successfully created ")
            return redirect("account")
    context = {"form":form}
    return render(response, "users/skill-form.html",context)


@login_required(login_url="create-skill")
def updateSkill(response,pk):
    profile = response.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)

    if response.method == "POST":
        form = SkillForm(response.POST,instance=skill)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(response,"The skill was successfully updated")
            return redirect("account")
    context = {"form": form}
    return render(response, "users/skill-form.html", context)


@login_required(login_url="login")
def deleteSkill(response,pk):
    profile = response.user.profile
    skill = profile.skill_set.get(id=pk)
    context = {"object":skill}

    if response.method == "POST":
        skill.delete()
        messages.success(response,"The skill was successfully deleted")
        return redirect("account")
    return render(response,"delete-template.html",context)
