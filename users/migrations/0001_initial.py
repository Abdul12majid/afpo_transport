# Generated by Django 5.1 on 2024-10-11 15:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('transport_app', '0002_role'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', models.CharField(max_length=255)),
                ('date_of_birth', models.DateTimeField(auto_now=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_images')),
                ('profile_bio', models.TextField(blank=True, max_length=500, null=True)),
                ('bookings_made', models.ManyToManyField(blank=True, to='transport_app.ride')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
