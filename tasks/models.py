from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    mobile = models.CharField(max_length=15, unique=True, null=True, blank=True)  

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",
        blank=True
    )

class Task(models.Model): # Model structure define here. 
    task_name = models.CharField(max_length=255)  
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task_type = models.CharField(max_length=50)
    completed_at = models.CharField(max_length=50, default="Work in progress")  
    status = models.CharField(max_length=20, default="Pending")  
    assigned_users = models.ManyToManyField(User, related_name="tasks")

    def __str__(self):
        return self.task_name
