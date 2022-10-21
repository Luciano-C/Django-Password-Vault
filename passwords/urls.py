from django.urls import path
from .views import *


# Viene de django y sirve para links 
#app_name = "passwords" 

urlpatterns = [
    path("", home, name="home"),
    path("signin/", signin, name="signin"),
    path("signup/", signup, name="signup"),
    path("signout/", signout, name="signout"),
    path("passwords/", passwords, name="passwords")
]