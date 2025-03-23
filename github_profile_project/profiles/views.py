from django.shortcuts import render, get_object_or_404
from .models import UserProfile, Repository

def profile(request, username):
    user_profile = get_object_or_404(UserProfile, username=username)
    repositories = Repository.objects.filter(user_profile=user_profile).order_by('-stars')
    return render(request, 'profiles/profile.html', {'user_profile': user_profile, 'repositories': repositories})