from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import phone_validator

# Create your models here.


class User(AbstractUser):
    # username = models.CharField(max_length=50, null=True, blank=True, unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15,unique=True, validators=[phone_validator,])

    def __str__(self):
        return ' '.join([self.first_name, self.last_name])
