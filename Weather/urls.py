from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('weather-history/', views.weather_history, name='weather_history'),
]
