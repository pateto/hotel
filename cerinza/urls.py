from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('english/', views.english, name='english'),
    path('habitacion/<str:room_name>/', views.room_detail, name='room_detail'),
    path('english/room/<str:room_name>/', views.room_detail_en, name='room_detail_en'),
]
