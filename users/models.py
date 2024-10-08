from django.db import models
from transport_app.models import Ride

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