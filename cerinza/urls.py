from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('english/', views.english, name='english'),
    path('habitacion/<str:room_name>/', views.room_detail, name='room_detail'),
    path('espacio/<str:space_name>/', views.space_detail, name='space_detail'),
    path('english/room/<str:room_name>/', views.room_detail_en, name='room_detail_en'),
    path('english/space/<str:space_name>/', views.space_detail_en, name='space_detail_en'),
]
