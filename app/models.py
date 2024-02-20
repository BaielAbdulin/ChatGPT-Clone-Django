from django.db import models
from django.contrib.auth.models import User

# Define Message Database Model
# Stores question, AI answer, time created, and foreign key to user
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)