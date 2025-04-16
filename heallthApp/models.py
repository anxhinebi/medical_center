from django.db import models
from django.conf import settings

class Doctor(models.Model):
    doctor_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="doctor_photos/", null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100, default="Unknown Service")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="services", to_field="doctor_id")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=1500, null=True, blank=True)
    photo = models.ImageField(upload_to="service_photos/", null=True, blank=True)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="reservations")
    full_name = models.CharField(max_length=50, default="Unknown Client")
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Booking for {self.full_name} - {self.service.name}"
