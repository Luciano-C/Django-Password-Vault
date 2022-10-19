from django.contrib import admin
from .models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    search_fields = ('email', 'name')
    list_display = ('email', 'name', 'is_active', 'is_staff', 'is_superuser')



admin.site.register(User, UserAdmin)