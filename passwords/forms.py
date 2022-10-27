from socket import fromshare
from django import forms
from .models import PasswordInfo

class PasswordForm(forms.ModelForm):
    class Meta():
        model = PasswordInfo
        fields = ["name", "address", "user_or_email", "password", "additional_notes", "type_of_password"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control mb-2", "placeholder": "Write a name"}),
            "address": forms.TextInput(attrs={"class": "form-control mb-2", "placeholder": "Write an address"}),
            "user_or_email": forms.TextInput(attrs={"class": "form-control mb-2", "placeholder": "Write your username o email"}),
            "password": forms.TextInput(attrs={"class": "form-control mb-2", "placeholder": "Write your password"}),
            "additional_notes": forms.Textarea(attrs={"class": "form-control mb-2", "placeholder": "Write your notes"}),
            "type_of_password": forms.TextInput(attrs={"class": "form-control mb-2", "placeholder": "Write your type of password"})
        }


class SearchByNameForm(forms.ModelForm):
    class Meta():
        model = PasswordInfo
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control mb-2", "placeholder": "Write a name"})
        }