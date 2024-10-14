from django.db import models
from transport_app.models import Ride, Account
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=255)
    date_of_birth=models.DateTimeField(auto_now=True)
    profile_image = models.ImageField(upload_to='profile_images', null=True, blank=True)
    profile_bio=models.TextField(null=True, blank=True, max_length=500)
    bookings_made = models.ManyToManyField(Ride, symmetrical=False, blank=True)

    def __str__(self):
        return self.user.username


class RiderProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.user.owner.username} Profile'

class DriverProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.user.owner.username} Profile'

@receiver(post_save, sender=Account)
def create_profile(sender, instance, created, **kwargs):
    
    if created:
        if instance.role.name == "Rider":
            RiderProfile.objects.create(user=instance)
        else:
            DriverProfile.objects.create(user=instance)