from django.db import models
from datetime import date


class TravelModel(models.Model):

    agency_id = models.AutoField(primary_key=True)

    agency_name = models.TextField(verbose_name='Agency_Name', db_column="agency_name", max_length=50, blank=False,
                                  null=False)
    agency_pan_number = models.CharField(verbose_name='Agency_Pan_number', db_column="agency_pan_number", max_length=50, blank=False,
                                  null=False)
    agency_addres = models.CharField(verbose_name='Agency_Addres', db_column="agency_Addres", max_length=50, blank=False,
                                  null=False)
    agency_phone = models.BigIntegerField(verbose_name='Agency_Phone', db_column="agency_phone",  blank=False,
                                  null=False)
    agency_email = models.EmailField(db_column='agency_email', verbose_name='Agency_Email', max_length=100, null=True, blank=True)
    
    agency_pwd=models.CharField(verbose_name='Agency_Password',db_column="agency_pwd",max_length=100,blank=False,null=False)
    
    agency_photo = models.ImageField(verbose_name='Agency_Photo', db_column="agency_photo", upload_to='travel/images/', blank=False,)
    
    iata_certificate = models.ImageField(verbose_name='IATA_Certificate', db_column="iata_certificate", upload_to='travel/certificate/', blank=False,
                                   null=False)
    status = models.CharField(default = 'pending', max_length = 100, null=True)
    

    class Meta:
        db_table='travel_details'


class CardashboardModel(models.Model):
    
    car_id = models.AutoField(primary_key=True)
    agency_id=models.IntegerField(null=True,blank=True)
    car_type = models.CharField(verbose_name='Car_type', db_column="car_type", max_length=50, blank=False,
                                  null=False)
    car_model = models.CharField(verbose_name='Car_model', db_column="car_model", max_length=50, blank=False,
                                  null=False)
    car_no = models.CharField(verbose_name='Car_no', db_column="car_no", max_length=50, blank=False,
                                  null=False)
    select_car = models.CharField(verbose_name='Select_car', db_column="select_car", max_length=50, blank=False,
                                  null=False)
    price = models.CharField(db_column='price', verbose_name='Price', max_length=100, null=True, blank=True)
    
    
    car_photo = models.ImageField(verbose_name='Car_photo', db_column="car_photo", upload_to='car/images/', blank=False,)
    class Meta:
        db_table='car_dashboard'


class FlightdashboardModel(models.Model):
    
    flight_id = models.AutoField(primary_key=True)
    agency_id=models.IntegerField(null=True,blank=True)

    flight_name = models.CharField(verbose_name='Flight_name', db_column="flight_name", max_length=50, blank=False,
                                  null=False)
    flight_no = models.CharField(verbose_name='Flight_no', db_column="flight_no", max_length=50, blank=False,
                                  null=False)
    select_class = models.CharField(verbose_name='Select_class', db_column="select_class", max_length=50, blank=False,
                                  null=False)
    flight_from = models.CharField(verbose_name='From', db_column="trom", max_length=50, blank=False,
                                  null=False)
    to = models.CharField(verbose_name='To', db_column="to", max_length=50, blank=False,
                                  null=False)
    via = models.CharField(verbose_name='Via', db_column="via", max_length=50, blank=False,
                                  null=False)
    date = models.DateField(verbose_name='Date', db_column="date", max_length=50, blank=False,
                                  null=False)

    check_in = models.TimeField(verbose_name='Check_in', db_column="check_in", max_length=50, blank=False,
                                  null=False)

    check_out = models.TimeField(verbose_name='Check_out', db_column="check_out", max_length=50, blank=False,
                                  null=False)
    price = models.CharField(db_column='price', verbose_name='Price', max_length=100, null=True, blank=True)
    
    
    flight_photo = models.ImageField(verbose_name='Flight_photo', db_column="flight_photo", upload_to='flight/images/', blank=False,)
    class Meta:
        db_table='flight_dashboard'


class CruisesdashboardModel(models.Model):
    
    cruises_id = models.AutoField(primary_key=True)

    agency_id=models.IntegerField(null=True,blank=True)
    cruises_name = models.TextField(verbose_name='Cruises_name', db_column="cruises_name", max_length=50, blank=False,
                                  null=False)
    cruises_no = models.CharField(verbose_name='Cruises_no', db_column="cruises_no", max_length=50, blank=False,
                                  null=False)
    select_class = models.CharField(verbose_name='Select_class', db_column="select_class", max_length=50, blank=False,
                                  null=False)
    cruises_from = models.CharField(verbose_name='From', db_column="from", max_length=50, blank=False,
                                  null=False)
    to = models.CharField(verbose_name='To', db_column="to", max_length=50, blank=False,
                                  null=False)
    via = models.CharField(verbose_name='Via', db_column="via", max_length=50, blank=False,
                                  null=False)
    date = models.DateField(verbose_name='Date', db_column="date", max_length=50, blank=False,
                                  null=False)

    check_in = models.TimeField(verbose_name='Check_in', db_column="check_in", max_length=50, blank=False,
                                  null=False)

    check_out = models.TimeField(verbose_name='Check_out', db_column="check_out", max_length=50, blank=False,
                                  null=False)
    price = models.CharField(db_column='price', verbose_name='Price', max_length=100, null=True, blank=True)
    
    
    cruises_photo = models.ImageField(verbose_name='Cruises_photo', db_column="cruises_photo", upload_to='cruises/images/', blank=False,)
    class Meta:
        db_table='cruises_dashboard'