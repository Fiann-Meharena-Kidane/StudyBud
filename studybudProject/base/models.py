from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Room(models.Model):
    # host
    # topic
    name=models.CharField(max_length=200)
    description=models.TextField(null=True, blank=True)
    # participants=
    created=models.DateTimeField(auto_now_add=True)
    # updated=model.models.DateTimeField(auto_now=True)
    
    
    
    def __str__(self):
        return self.name 