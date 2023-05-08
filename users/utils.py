from .models import Profile, Skill
from django.db.models import Q


def searchProfiles(response):
    search_query = ''

    if response.GET.get('search_query'):
        search_query = response.GET.get('search_query')

    skills = Skill.objects.filter(name__icontains=search_query)
    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(short_intro__icontains=search_query) |
        Q(skill__in=skills)
    )
    context = {"profiles": profiles, "search_query": search_query}

    return profiles, search_query