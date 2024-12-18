from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Run(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=2000, null=True, blank=True)
    model_name = models.CharField(max_length=255, null=True, blank=True)
    input_data = models.JSONField(null=True, blank=True)
    output_data = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
