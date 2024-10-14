from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Role(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name

def get_default_role():
    try:
        return Role.objects.get(name="Rider")
    except Role.DoesNotExist:
        return None


class Account(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, default=get_default_role)

    def __str__(self):
        return f'{self.owner.username} {self.role.name}'

class Ride(models.Model):
    rider = models.ForeignKey(User, on_delete=models.CASCADE)
    driver = models.ForeignKey(User, related_name="host", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
    	return self.rider.username