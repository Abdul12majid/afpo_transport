from django.contrib import admin
from .models import Role, Account, Ride

# Register your models here.
admin.site.register(Account)
admin.site.register(Role)
admin.site.register(Ride)