from django.db import models


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=255) # Room Name
    capacity = models.IntegerField(null=False) # Room Capacity
    projector = models.BooleanField(default=True) # presence of the projector

