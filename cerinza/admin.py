from django.contrib import admin
from .models import Room, Guest, Booking

from django.db.models import Sum

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
	list_display = ("id", "start_date", "end_date", "room", "price_cop", "guests_list")

	def price_cop(self, obj):
		return f"${obj.price:,.0f} COP"
	price_cop.short_description = "Price (COP)"

	def guests_list(self, obj):
		return ", ".join(str(guest) for guest in obj.guests.all())
	guests_list.short_description = "Guests"

admin.site.register(Room)
admin.site.register(Guest)
