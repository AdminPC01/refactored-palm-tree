from django.shortcuts import render
from .models import Profile
# Create your views here.
def profiles(response):
    profiles = Profile.objects.all()
    return render(response,"users/profiles.html",{"profiles":profiles })

def userProfile(response,pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    context = {"profile":profile,"topSkills":topSkills,"otherSkills":otherSkills}
    return render(response,"users/user-profile.html", context)