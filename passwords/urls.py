from django.urls import path
from .views import *


# Viene de django y sirve para links 
#app_name = "passwords" 

urlpatterns = [
    path("", home, name="home"),
    path("signin/", signin, name="signin"),
    path("signup/", signup, name="signup"),
    path("signout/", signout, name="signout"),
    path("passwords/", passwords, name="passwords"),
    path("passwords/<int:password_id>", password_detail, name="password_detail"),
    path("passwords/<int:password_id>/delete", delete_password, name="delete_password"),
    path("passwords/create", create_password, name="create_password")
]