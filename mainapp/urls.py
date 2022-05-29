from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('admin', views.admin, name='admin'),
    path('hotel', views.hotel, name='hotel'),
    

    

    path('car', views.car, name='car'),
    path('flight', views.flight, name='flight'),
    path('main_cruises', views.main_cruises, name='main_cruises'),
    
    

   
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('hotel_corporate', views.hotel_corporate, name='hotel_corporate'),
    path('car_rental', views.car_rental, name='car_rental'),
    path('cruises_dashboard', views.cruises_dashboard, name='cruises_dashboard'),
    path('admin_feedback', views.admin_feedback, name='admin_feedback'),
    path('flight_dashboard', views.flight_dashboard, name='flight_dashboard'),
    path('admin_profile', views.admin_profile, name='admin_profile'),
    path('travel_agency', views.travel_agency, name='travel_agency'),

    path('accept_agency/<int:id>/', views.accept_agency, name='accept_agency'),
    path('reject_agency/<int:id>/', views.reject_agency, name='reject_agency'),
    path('accept_corporate/<int:id>/', views.accept_corporate, name='accept_corporate'),
    path('reject_corporate/<int:id>/', views.reject_corporate, name='reject_corporate'),


]


