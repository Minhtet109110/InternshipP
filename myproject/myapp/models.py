from django.db import models
from django.shortcuts import render
from django.contrib.auth.models import User
# Create your models here.
class Project(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.title

def project_list(reqduest):
    project = Project.objects.all()
    return render(reqduest,'project_list.html',{'project':project})


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)

    def str(self):
        return self.user.username
