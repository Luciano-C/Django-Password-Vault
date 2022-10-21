from django.db import models
from authuser.models import User
from django import forms

# Create your models here.
class PasswordInfo(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    user_or_email = models.CharField(max_length=100)
    #password = forms.CharField(max_length=200, widget=forms.PasswordInput)
    password = models.CharField(max_length=200)
    additional_notes = models.TextField(blank=True)
    type_of_password = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'password_info'
        verbose_name = 'Password Info'
        verbose_name_plural = 'Password Info'
        
        
