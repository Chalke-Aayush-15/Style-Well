from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.shortcuts import render
from Home.models import Appointment
from django.db.models import Q
# from .models import Service

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

# @login_required
# def userDashboard(request):
#     now = timezone.now()

#     next_appointment = (
#         Appointment.objects
#         .filter(
#             user=request.user,
#             status='confirmed'
#         )
#         .filter(
#             Q(date__gt=now.date()) |
#             Q(date=now.date(), time__gte=now.time())
#         )
#         .order_by('date', 'time')
#         .first()
#     )

#     return render(request, 'user_dashboard.html', {
#         'next_appointment': next_appointment
#     })


@login_required
def userDashboard(request):
    now = timezone.now()

    upcoming_appointments = Appointment.objects.filter(
        user=request.user,
        status='confirmed'
    ).filter(
        Q(date__gt=now.date()) |
        Q(date=now.date(), time__gte=now.time())
    ).order_by('date', 'time')

    return render(request, 'user_dashboard.html', {
        'upcoming_appointments': upcoming_appointments,
        'next_appointment': upcoming_appointments.first(),  # optional highlight
    })

def logout_view(request):
    logout(request)
    return redirect('home')

def haircuts(request):
    return render(request, 'haircuts.html')

def beard_types(request):
#     services = Service.objects.filter(category='beard')  # optional
    return render(request, 'beardtypes.html'
    )

def hairstyling(request):
    return render(request, 'hairstylingtypes.html')






def hair_treatments(request):
    return render(request, 'hairtreatments_types.html')

@login_required
def admin_dashboard(request):
    return render(request, 'admin-dashboard.html')