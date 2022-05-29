from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views 
from django.core.mail import EmailMessage

urlpatterns = [
    
    path('customer_registration', views.customer_registration, name='customer_registration'),
    path('customer', views.customer, name='customer'),
    path('room', views.room, name='room'),
    path('user_car_rental', views.user_car_rental, name='user_car_rental'),
    path('user_flight', views.user_flight, name='user_flight'),
    path('user_cruises', views.user_cruises, name='user_cruises'),
    path('booking/<int:id>', views.booking, name='booking'),
    path('car_booking/<int:id>', views.car_booking, name='car_booking'),
    path('flight_booking/<int:id>', views.flight_booking, name='flight_booking'),
    path('cruises_booking/<int:id>', views.cruises_booking, name='cruises_booking'),

    path('password_reset',views.password_reset,name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name="resetpws/password-reset-done.html"),name='password_reset_done'),
    path('password_reset_confirm',views.password_reset_confirm, name='password_reset_confirm'),
    path('password_reset_complete/done/',auth_views.PasswordResetCompleteView.as_view(template_name="resetpws/password-reset-complete.html"),name='password_reset_complete'),
    
    path('user_profile', views.user_profile, name='user_profile'),
    # path('user_feedback', views.user_feedback, name='user_feedback'),
    path('my_feedback', views.my_feedback, name='my_feedback'),
    path('user_hotel_feedback/<int:id>/<email>', views.user_hotel_feedback, name='user_hotel_feedback'),
    path('user_agency_feedback/<int:id>/<email>', views.user_agency_feedback, name='user_agency_feedback'),
    
    
    path('base', views.base, name='base'),
    path('my_booking', views.my_booking, name='my_booking'),

    path('updateprofile', views.updateprofile, name='updateprofile'),
    path('updateprofile/<int:id>', views.updateprofile, name='updateprofile'),





    ]