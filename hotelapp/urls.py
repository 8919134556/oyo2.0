from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

path('hotel_registration', views.hotel_registration, name='hotel_registration'),
path('hotel_owners', views.hotel_owners, name='hotel_owners'),
path('hotel_index', views.hotel_index, name='hotel_index'),

path('add_room', views.add_room, name='add_room'),
path('edit_room', views.edit_room, name='edit_room'),
path('deleroom/<int:id>', views.deleroom, name='deleroom'),
path('updateroom', views.updateroom, name='updateroom'),
path('updateroom/<int:id>', views.updateroom, name='updateroom'),

path('edit_room_form', views.edit_room_form, name='edit_room_form'),
path('hotel_feedback', views.hotel_feedback, name='hotel_feedback'),

path('hotel_profile', views.hotel_profile, name='hotel_profile'),
path('view_room', views.view_room, name='view_room'),
path('view_booking', views.view_booking, name='view_booking'),

]
