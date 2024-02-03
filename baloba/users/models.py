from django.db import models
from django.contrib.auth.models import AbstractUser
from baloba.utils.base import BaseModel
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    
    # USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = ["username"]
    

class UserProfile(BaseModel):
    USER_TYPES = (
        (1, 'Viewer'),
        (2, 'Publisher'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    user_type = models.IntegerField(choices=USER_TYPES, default=1)
    about = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.user