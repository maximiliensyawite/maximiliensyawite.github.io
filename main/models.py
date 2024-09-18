from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='services/')

    def __str__(self):
        return f"{self.title} - {self.price} FC/heure"

class GalleryItem(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')

class Expert(models.Model):
    name = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)
    image = models.ImageField(upload_to='experts/')

class Partner(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    # autres champs nécessaires

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Ajoutez ici d'autres champs pour le profil utilisateur si nécessaire
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('regular', 'Utilisateur régulier'),
        ('special', 'Partenaire'),
        ('admin', 'Administrateur'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='regular')

class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Reservation for {self.service.title} by {self.user.username}"
