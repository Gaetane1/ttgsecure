from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Message(models.Model):
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    binaire = models.TextField()
    date_envoye = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message {self.id} de {self.auteur.username}"
    

