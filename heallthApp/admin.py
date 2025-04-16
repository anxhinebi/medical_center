from django.utils.html import format_html
from django.contrib import admin
from .models import Doctor, Service, Reservation

@admin.register(Doctor)
class DoctorsAdmin(admin.ModelAdmin):
    list_display = ["doctor_id", "name", "display_photo", "description"]
    search_fields = ["name"]

    def display_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:5px"/>', obj.photo.url)
        return "No Image"
    display_photo.short_description = "Photo"

@admin.register(Service)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ["name", "doctor", "price", "description", "display_photo"]
    list_filter = ["doctor"]
    
    def display_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:5px"/>', obj.photo.url)
        return "No Image"
    display_photo.short_description = "Photo"

@admin.register(Reservation)
class ReservationsAdmin(admin.ModelAdmin):
    list_display = ["service", "full_name", "date", "time"]
    list_filter = ["date"]