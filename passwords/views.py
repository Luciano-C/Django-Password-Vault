from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signin(request):
    if request.method == "GET":
        return render(request, 'signin.html')

def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')