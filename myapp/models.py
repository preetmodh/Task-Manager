from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime

# Create your models here.

class User(AbstractUser):
    pass

class Content(models.Model):
    id=models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist")
    body = models.CharField(max_length=700,blank=True)
    name = models.CharField(max_length=20,blank=True,editable=False)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=datetime.now())

    def __str__(self):
	    return self.name
