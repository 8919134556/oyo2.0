from django.db import models
from datetime import date


class UserModel(models.Model):

    user_id = models.AutoField(primary_key=True)


    user_name = models.TextField(verbose_name='User_Name', db_column="user_name", max_length=50, blank=False,
                                  null=False)
    user_lastname = models.TextField(verbose_name='User_lastname', db_column="user_lastname", max_length=50, blank=False,
                                  null=False)
    user_phone = models.BigIntegerField(verbose_name='User_Phone', db_column="user_phone", blank=False,
                                  null=False)
    user_email = models.EmailField(db_column='user_email', verbose_name='User_Email', max_length=100, null=True, blank=True)
    
    user_pwd=models.CharField(verbose_name='User_Password',db_column="user_pwd",max_length=100,blank=False,null=False)
    
    user_photo = models.ImageField(verbose_name='User_Photo', db_column="user_photo", upload_to='user/images/', blank=False,
                                   null=True)

    class Meta:
        db_table='user_details'




class RoomBooking (models.Model):
    
    booking_id = models.AutoField(primary_key=True)
    room_id=models.IntegerField(null=True,blank=True)

    room_addres = models.CharField(verbose_name='Room_Addres', db_column="room_Addres", max_length=50, blank=False,
                                  null=False)
    room_check_in = models.DateField(verbose_name='Room_Check_In', db_column="room_check_in", max_length=50, blank=False,
                                  null=False)
    room_check_out = models.DateField(verbose_name='Room_Check_Out', db_column="room_check_out", max_length=50, blank=False,
                                  null=False)
    no_room = models.CharField(verbose_name='No_Rooms', db_column="no_rooms", max_length=50, blank=False,
                                  null=False)
    no_adults = models.CharField(verbose_name='No_Adults', db_column="no_adults", max_length=50, blank=False,
                                  null=False)
    no_children = models.CharField(verbose_name='No_Children', db_column="no_children", max_length=50, blank=False,
                                  null=False)
    email = models.EmailField(verbose_name='Email', db_column="email", max_length=50, blank=False,
                                  null=False)
    phone = models.CharField(verbose_name='Phone', db_column="phone", max_length=50, blank=False,
                                  null=False)

    class Meta:
        db_table='booking_room_details'

class CarBooking (models.Model):
    car_booking_id = models.AutoField(primary_key=True)
    agency_id=models.IntegerField(null=True,blank=True)
    car_from = models.CharField(verbose_name='Car_from', db_column="car_from", max_length=50, blank=False,
                                  null=False)
    to = models.CharField(verbose_name='To', db_column="to", max_length=50, blank=False,
                                  null=False)
    journey_date = models.DateField(verbose_name='Journey_Date', db_column="journey_date", max_length=50, blank=False,
                                  null=False)
    return_date = models.DateField(verbose_name='Return_Date', db_column="return_date", max_length=50, blank=False,
                                  null=False)
    pick_up = models.CharField(verbose_name='Pick_Up', db_column="pick_up", max_length=50, blank=False,
                                  null=False)
    drop_off = models.CharField(verbose_name='Drop_Off', db_column="drop_off", max_length=50, blank=False,
                                  null=False)
    email = models.EmailField(verbose_name='Email', db_column="email", max_length=50, blank=False,
                                  null=False)
    phone = models.CharField(verbose_name='Phone', db_column="phone", max_length=50, blank=False,
                                  null=False)

    class Meta:
        db_table='booking_car_details'


class FlightBooking (models.Model):
    flight_booking_id = models.AutoField(primary_key=True)
    agency_id=models.IntegerField(null=True,blank=True)
    addres = models.CharField(verbose_name='Addres', db_column="addres", max_length=50, blank=False,
                                  null=False)
    check_in = models.DateField(verbose_name='Check_in', db_column="check_in", max_length=50, blank=False,
                                  null=False)
    check_out = models.DateField(verbose_name='Check_Out', db_column="check_out", max_length=50, blank=False,
                                  null=False)
    passport = models.CharField(verbose_name='Passport', db_column="passport", max_length=50, blank=False,
                                  null=False)
    select_class = models.CharField(verbose_name='Select_Class', db_column="select_class", max_length=50, blank=False,
                                  null=False)
    no_adults = models.CharField(verbose_name='No_Adults', db_column="no_adults", max_length=50, blank=False,
                                  null=False)
    no_children = models.CharField(verbose_name='No_Children', db_column="no_children", max_length=50, blank=False,
                                  null=False)
    email = models.EmailField(verbose_name='Email', db_column="email", max_length=50, blank=False,
                                  null=False)
    phone = models.CharField(verbose_name='Phone', db_column="phone", max_length=50, blank=False,
                                  null=False)

    class Meta:
        db_table='booking_flight_details'

class CruisesBooking (models.Model):
    cruises_booking_id = models.AutoField(primary_key=True)
    agency_id=models.IntegerField(null=True,blank=True)
    addres = models.CharField(verbose_name='Addres', db_column="addres", max_length=50, blank=False,
                                  null=False)
    check_in = models.DateField(verbose_name='Check_in', db_column="check_in", max_length=50, blank=False,
                                  null=False)
    check_out = models.DateField(verbose_name='Check_Out', db_column="check_out", max_length=50, blank=False,
                                  null=False)
    passport = models.CharField(verbose_name='Passport', db_column="passport", max_length=50, blank=False,
                                  null=False)
    select_class = models.CharField(verbose_name='Select_Class', db_column="select_class", max_length=50, blank=False,
                                  null=False)
    no_adults = models.CharField(verbose_name='No_Adults', db_column="no_adults", max_length=50, blank=False,
                                  null=False)
    no_children = models.CharField(verbose_name='No_Children', db_column="no_children", max_length=50, blank=False,
                                  null=False)
    email = models.EmailField(verbose_name='Email', db_column="email", max_length=50, blank=False,
                                  null=False)
    phone = models.CharField(verbose_name='Phone', db_column="phone", max_length=50, blank=False,
                                  null=False)

    class Meta:
        db_table='booking_cruises_details'


class UserFb (models.Model):
    fb_id = models.AutoField(primary_key=True)
    rating = models.CharField (verbose_name = 'Rating', db_column="rating", max_length=50, blank=False, null=False)
    hotel_id = models.CharField (verbose_name = 'Hotel_id', db_column="hotel_id", max_length=50, blank=False, null=True)
    comments = models.TextField(verbose_name='Comments', db_column="comments", max_length=50, blank=False,
                                  null=False)
    agency_id = models.CharField(verbose_name='Agency_id', db_column="agency_id", max_length=50, blank=False,
                                  null=False)
    class Meta:
        db_table='user_fb'
