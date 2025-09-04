from django.db import models


# Create your models here.
# users/models.py

from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = [("male", "Male"), ("female", "Female")]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to="profile_pics/", null=True, blank=True)
    preferences = models.JSONField(blank=True, null=True)  

    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)      


    def __str__(self):
        return f"{self.user.username} Profile"
