from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.shortcuts import render
from Home.models import Appointment

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

def adminDashboard(request):
    return render(request, 'admin-dashboard.html')

def userDashboard(request):
    return render(request, 'user_dashboard.html')


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # 1️⃣ Password match check
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect("register")

        # 2️⃣ Username exists check
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        # 3️⃣ Email exists check
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect("register")

        # 4️⃣ Create user (PASSWORD IS HASHED AUTOMATICALLY ✅)
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Account created successfully")
        return redirect("login")   # or home

    return render(request, "register.html")


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(
                request,
                username=user_obj.username,
                password=password
            )
        except User.DoesNotExist:
            user = None

        if user is not None:
            login(request, user)

            if user.is_superuser:
                return redirect('adminDashboard')
            else:
                return redirect('userDashboard')
        else:
            messages.error(request, "Invalid email or password")
            return redirect('login')

    return render(request, 'login.html')


def dashboard(request):
    now = timezone.now()

    next_appointment = (
        Appointment.objects
        .filter(
            user=request.user,
            status='confirmed',
            date__gte=now.date()
        )
        .order_by('date', 'time')
        .first()
    )

    context = {
        'next_appointment': next_appointment,
    }
    return render(request, 'dashboard/home.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')