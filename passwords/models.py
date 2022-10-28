from django.db import models
from authuser.models import User
from django import forms

# Create your models here.
class PasswordInfo(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250, blank=True)
    user_or_email = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=200, blank=True)
    additional_notes = models.TextField(blank=True)
    type_of_password = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'password_info'
        verbose_name = 'Password Info'
        verbose_name_plural = 'Password Info'
        
        
