from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import phone_validator

# Create your models here.


class User(AbstractUser):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15, validators=[phone_validator,])
