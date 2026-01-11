"""
URL configuration for StyleWell project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from Home import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index, name='home'),
    path('features/', views.features, name='features'),
    path('services/', views.services, name='services'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('contacts/', views.contacts, name='contacts'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('adminDashboard/', views.adminDashboard, name='adminDashboard'),
    path('userDashboard/', views.userDashboard, name='userDashboard'),
    path('haircuts/', views.haircuts, name='haircuts'),
    path('beard-types/', views.beard_types, name='beard_types'),
    path('hairstyling/', views.hairstyling, name='hairstyling'),
    path('hairtreatments_types/',
    views.hair_treatments,
    name='hair_treatments'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


]
