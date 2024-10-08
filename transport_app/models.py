from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Ride(models.Model):
    rider = models.ForeignKey(User, on_delete=models.CASCADE)
    driver = models.ForeignKey(User, related_name="host", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
    	return self.rider.username