from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Guest(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.name or ''} {self.last_name or ''}".strip()

class Booking(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, blank=True, null=True)        
    price = models.DecimalField(max_digits=12, decimal_places=0, verbose_name="Price (COP)")
    guests = models.ManyToManyField(Guest, related_name="bookings")

    def __str__(self):
        return str(self.start_date)
    
