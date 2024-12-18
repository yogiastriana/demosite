from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    STATUS_CHOICES = [
        ('approved', 'Approved'),
        ('unapproved', 'Unapproved'),
    ]
    
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='unapproved')
    role = models.CharField(max_length=5, choices=ROLE_CHOICES, default='user')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
        ordering = ['user']  # Optional: Order by user field
