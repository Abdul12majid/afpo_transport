from django.contrib import admin
from .models import Profile, RiderProfile, DriverProfile
# Register your models here.

admin.site.register(Profile)
admin.site.register(RiderProfile)
admin.site.register(DriverProfile)