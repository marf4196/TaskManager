from django.db import models
from account.models import User

# Create your models here.


class Task(models.Model):
    CHOICES = (
        ('L', 'Low'),
        ('M', 'Meduim'),
        ('H', 'High'),
    )
    title = models.CharField(max_length=60)
    body = models.TextField()
    start_time = models.TimeField(null=True, blank=True, verbose_name='Starts at')
    end_time = models.TimeField(null=True, blank=True, verbose_name='Finishes in')
    planner = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.CharField(choices=CHOICES, max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)

    class Meta:
        ordering = ['done', '-start_time',]