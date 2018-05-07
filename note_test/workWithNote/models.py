from django.db import models
from datetime import date
import uuid
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Note(models.Model):
    header_note = models.CharField(max_length=64)
    unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    dt = models.DateTimeField(auto_now=True)
    text = models.TextField()
    favorites = models.BooleanField(default=False)

    def __str__(self):
        return self.header_note
