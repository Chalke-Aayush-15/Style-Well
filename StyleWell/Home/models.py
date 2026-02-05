from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

class UserAccount(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # will store hashed password

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Hash the password before saving (to avoid storing in plain text)
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
    
class Appointment(models.Model):
    STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('pending', 'Pending'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stylist = models.CharField(max_length=100)
    service = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    class Meta:
        ordering = ['date', 'time']  # important

    def __str__(self):
        return f"{self.user} - {self.date} {self.time}"
    
class Lookbook(models.Model):  # Changed to capital L for convention
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lookbooks')  # Added user field
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='lookbook_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']  # Show newest first

    def __str__(self):
        return f"{self.user.username} - {self.title or 'Untitled'}"
