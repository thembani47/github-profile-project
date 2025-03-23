from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.URLField(blank=True, null=True)  # URL to the profile picture
    location = models.CharField(max_length=200, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True) #Direct link to the github profile
    twitter_username = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username

class Repository(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='repositories')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=100, blank=True, null=True)
    stars = models.IntegerField(default=0)
    forks = models.IntegerField(default=0)
    repo_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name