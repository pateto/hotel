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

    autocomplete_fields = ["guests"]

    def guests_list(self, obj):
        return ", ".join(str(guest) for guest in obj.guests.all())
    guests_list.short_description = "Guests"

    def price_(self, obj):
        return f'{obj.price:,}'.replace(',', '.')
    price_.admin_order_field = 'price'
    

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "owner")
    list_filter = ("owner",)

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "last_name", "email", "phone")
    list_filter = ("name", "last_name")
    search_fields = ("name", "last_name", "email", "phone")
