from django.shortcuts import render
from .models import Profile
# Create your views here.
def profiles(response):
    profiles = Profile.objects.all()
    return render(response,"users/profiles.html",{"profiles":profiles })