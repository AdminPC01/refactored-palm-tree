from django.shortcuts import render

# Create your views here.
def profiles(response):
    return render(response,"users/profiles.html")