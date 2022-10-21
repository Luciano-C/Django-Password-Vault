from django.urls import path
from .views import *

# Viene de django y sirve para links 
app_name = "passwords" 

urlpatterns = [
    path("", home, name="home"),
    path("signin", signin, name="signin")
    #path("<int:post_id>", post_detail, name="post_detail")
]