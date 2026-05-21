from django.contrib import admin
from .models import Room, Guest, Booking
from rangefilter.filters import DateRangeQuickSelectListFilterBuilder
from admin_totals.admin import ModelAdminTotals
from django.db.models import Sum


@admin.register(Booking)
class BookingAdmin(ModelAdminTotals):
	
    list_display = ("id", "start_date", "end_date", "room", "guests_list", "price_")

    list_totals = [('price_', lambda field: Sum(field))]

    list_filter = (
        ("start_date", DateRangeQuickSelectListFilterBuilder()),
        "room"
        )
    
    def guests_list(self, obj):
        return ", ".join(str(guest) for guest in obj.guests.all())
    guests_list.short_description = "Guests"

    def price_(self, obj):
        return f'{obj.price:,}'.replace(',', '.')
    price_.admin_order_field = 'price'
    

admin.site.register(Room)
admin.site.register(Guest)
