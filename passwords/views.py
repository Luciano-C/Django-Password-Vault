from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from authuser.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import PasswordForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signin(request):
    if request.method == "GET":
        return render(request, 'signin.html')
    else:
        user = authenticate(
            request, email=request.POST['email'], password=request.POST['password']
        ) 
        
        if user is None:
            return render(request, 'signin.html', {
                'error': 'Email or password incorrect'
            })
        else:
            login(request, user)
            return redirect('passwords') 

def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(email=request.POST['email'])
                user.set_password(request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('passwords')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'error': 'Email already exists'
                })

@login_required            
def signout(request):
    logout(request)
    return redirect('home')

@login_required 
def passwords(request):
    user_passwords = PasswordInfo.objects.filter(user=request.user)
    return render(request, 'passwords.html', {
            'user_passwords': user_passwords
    })

@login_required
def password_detail(request, password_id):
    if request.method == "GET":
        password = get_object_or_404(PasswordInfo, pk=password_id, user=request.user)
        form = PasswordForm(instance=password)
        return render(request, 'password_detail.html', {
            'password': password,
            'form': form
        })
    else:
        try:
            password = get_object_or_404(PasswordInfo, pk=password_id, user=request.user)
            form = PasswordForm(request.POST, instance=password)
            form.save()
            return redirect('passwords')
        except ValueError:
            return render(request, 'password_detail.html', {
            'password': password,
            'form': form,
            'error': "Error updating password"
        }) 

   
@login_required
def delete_password(request, password_id):
    password = get_object_or_404(PasswordInfo, pk=password_id, user=request.user)
    if request.method == "POST":
        password.delete()
        return redirect('passwords')

@login_required
def create_password(request):
    if request.method == "GET":
        return render(request, 'create_password.html', {
            'form': PasswordForm
        })
    else:
        try:
            form = PasswordForm(request.POST)
            new_password = form.save(commit=False)
            new_password.user = request.user
            new_password.save()
            return redirect('passwords')
        except ValueError:
            return render(request, 'create_password.html', {
                'form': PasswordForm,
                'error': 'Invalid Data'
            })

@login_required 
def search_passwords_name(request):
    if request.GET['search_by_name'] != "":
        user_passwords = PasswordInfo.objects.filter(user=request.user).filter(name__icontains=request.GET['search_by_name'])
        return render(request, 'passwords.html', {
            'user_passwords': user_passwords,
            'value_name': request.GET['search_by_name']
        })
    else:
        return redirect('passwords')

@login_required 
def search_passwords_type(request):
    if request.GET['search_by_type'] != "":
        user_passwords = PasswordInfo.objects.filter(user=request.user).filter(type_of_password__icontains=request.GET['search_by_type'])
        return render(request, 'passwords.html', {
            'user_passwords': user_passwords,
            'value_type': request.GET['search_by_type']
        })
    else:
        return redirect('passwords')