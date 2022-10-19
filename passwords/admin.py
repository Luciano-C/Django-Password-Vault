from django.contrib import admin
from .models import *

# Register your models here.
class PasswordInfoAdmin(admin.ModelAdmin):
    search_fields = ('name', 'address', 'type_of_password')
    list_display = ('name', 'address', 'user_or_email', 'password', 'type_of_password')


admin.site.register(PasswordInfo, PasswordInfoAdmin)