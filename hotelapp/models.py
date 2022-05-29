from django.db import models
from datetime import date
# Create your models here.

class HotelModel(models.Model):
    
    hotel_id = models.AutoField(primary_key=True)

    hotel_name = models.CharField(verbose_name='Hotel_Name', db_column="hotel_name", max_length=50, blank=False,
                                  null=False)
    hotel_pan_number = models.CharField(verbose_name='Hotel_Pan_number', db_column="hotel_pan_number", max_length=50, blank=False,
                                  null=False)
    hotel_addres = models.CharField(verbose_name='Hotel_Addres', db_column="hotel_Addres", max_length=50, blank=False,
                                  null=False)
    hotel_phone = models.BigIntegerField(verbose_name='Hotel_Phone', db_column="hotel_phone", blank=False,
                                  null=False)
    hotel_email = models.EmailField(db_column='hotel_email', verbose_name='Hotel_Email', max_length=100, null=True, blank=True)
    
    hotel_pwd=models.CharField(verbose_name='Hotel_Password',db_column="hotel_pwd",max_length=100,blank=False,null=False)
    
    hotel_photo = models.ImageField(verbose_name='Hotel_Photo', db_column="hotel_photo", upload_to='hotel/images/', blank=False,)
    
    hotel_certificate = models.ImageField(verbose_name='Hotel_Certificate', db_column="hotel_certificate", upload_to='hotel/certificate/', blank=False,
                                   null=False)
    status = models.CharField(default = 'pending', max_length = 100, null=True)

    class Meta:
        db_table='hotel_details'




class HoteldashboardModel(models.Model):
    
    room_id = models.AutoField(primary_key=True)

    hotel_id=models.IntegerField(null=True,blank=True)
    
    room_type = models.CharField(verbose_name='Room_type', db_column="room_type", max_length=50, blank=False,
                                  null=False)
    room_size = models.CharField(verbose_name='Room_size', db_column="room_size", max_length=50, blank=False,
                                  null=False)
    check_in = models.TimeField(verbose_name='Check_in', db_column="check_in", max_length=50, blank=False,
                                  null=False)
    check_out = models.TimeField(verbose_name='Check_out', db_column="check_out", max_length=50, blank=False,
                                  null=False)
    price = models.CharField(db_column='price', verbose_name='Price', max_length=100, null=True, blank=True)
    
    description=models.CharField(verbose_name='Description',db_column="description",max_length=100,blank=False,null=False)
    hotel_policies=models.CharField(verbose_name='Hotel_policies',db_column="hotel_policies",max_length=100,blank=False,null=False)
    
    room_photo = models.ImageField(verbose_name='Room_photo', db_column="room_photo", upload_to='room/images/', blank=False,)
    
    
    

    class Meta:
        db_table='hotel_dashboard'







