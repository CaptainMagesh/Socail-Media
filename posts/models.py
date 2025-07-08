from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Post(models.Model):
    VISIBILITY_CHOICES = [("public", "Public"), ("private", "Private")]

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
def __str__(self):
        return f"{self.author} - {self.visibility}"