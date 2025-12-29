from django.shortcuts import render, redirect
from .models import UserAccount
from django.contrib import messages

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
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        UserAccount.objects.create(
            username=username,
            email=email,
            password=password1
        )

        messages.success(request, "Account created successfully!")
        return redirect('login')

    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

