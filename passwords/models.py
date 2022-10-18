from django.db import models

# Create your models here.
class PasswordInfo(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    user_or_email = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    additional_notes = models.TextField(blank=True)
    type_of_password = models.CharField(max_length=100)


    def __str__(self):
        return self.name
