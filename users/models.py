from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    STATUT_CHOICES = (
        ('client', 'Client'),
        ('admin', 'Admin'),
    )
    statut = models.CharField(max_length=10, choices=STATUT_CHOICES, default='client')
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    adresse = models.TextField(blank=True)
    telephone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.username
