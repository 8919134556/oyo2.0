from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    
    path('travel_registration', views.travel_registration, name='travel_registration'),
    path('travel_agencies', views.travel_agencies, name='travel_agencies'),
    path('travel_index', views.travel_index, name='travel_index'),





    path('cars', views.cars, name='cars'),
    path('edit_cars', views.edit_cars, name='edit_cars'),
    path('edit_car_form', views.edit_car_form, name='edit_car_form'),
    path('cruises', views.cruises, name='cruises'),
    path('edit_cruises', views.edit_cruises, name='edit_cruises'),
    path('edit_cruises_form', views.edit_cruises_form, name='edit_cruises_form'),
    path('edit_details', views.edit_details, name='edit_details'),
    path('view_details', views.view_details, name='view_details'),
    path('view_booking_details', views.view_booking_details, name='view_booking_details'),
    path('car_booking_details', views.car_booking_details, name='car_booking_details'),
    path('flight_booking_details', views.flight_booking_details, name='flight_booking_details'),
    path('cruises_booking_details', views.cruises_booking_details, name='cruises_booking_details'),
    path('view_cars', views.view_cars, name='view_cars'),
    path('view_flights', views.view_flights, name='view_flights'),
    path('view_cruises', views.view_cruises, name='view_cruises'),
    path('travel_flight', views.travel_flight, name='travel_flight'),
    path('edit_flight_form', views.edit_flight_form, name='edit_flight_form'),
    path('edit_flight', views.edit_flight, name='edit_flight'),
    path('feedback', views.feedback, name='feedback'),
    path('profile', views.profile, name='profile'),
    path('delecar/<int:id>', views.delecar, name='delecar'),
    path('deleflight/<int:id>', views.deleflight, name='deleflight'),
    path('delecruises/<int:id>', views.delecruises, name='delecruises'),
    path('updatecar', views.updatecar, name='updatecar'),
    path('updatecar/<int:id>', views.updatecar, name='updatecar'),
    path('updateflight', views.updateflight, name='updateflight'),
    path('updateflight/<int:id>', views.updateflight, name='updateflight'),
    path('updatecruises', views.updatecruises, name='updatecruises'),
    path('updatecruises/<int:id>', views.updatecruises, name='updatecruises'),
   
    ]