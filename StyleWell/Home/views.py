from django.shortcuts import render, redirect
from .models import UserAccount
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'home.html')

def features(request):
    return render(request, 'features.html')

def services(request):
    return render(request, 'services.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def contacts(request):
    return render(request, 'contacts.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password")
        password2 = request.POST.get("confirm_password")

        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        # Save (add hashing for safety)
        from django.contrib.auth.hashers import make_password
        UserAccount.objects.create(
            username=username,
            email=email,
            password=make_password(password1)
        )

        messages.success(request, "Account created successfully!")
        return redirect('login')  # or home

    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('home')