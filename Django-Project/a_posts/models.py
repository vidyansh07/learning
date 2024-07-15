from django.db import models
import uuid

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    image = models.URLField(max_length=250)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    