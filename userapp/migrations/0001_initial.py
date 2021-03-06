# Generated by Django 3.2.8 on 2022-03-24 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarBooking',
            fields=[
                ('car_booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('agency_id', models.IntegerField(blank=True, null=True)),
                ('car_from', models.CharField(db_column='car_from', max_length=50, verbose_name='Car_from')),
                ('to', models.CharField(db_column='to', max_length=50, verbose_name='To')),
                ('journey_date', models.DateField(db_column='journey_date', max_length=50, verbose_name='Journey_Date')),
                ('return_date', models.DateField(db_column='return_date', max_length=50, verbose_name='Return_Date')),
                ('pick_up', models.CharField(db_column='pick_up', max_length=50, verbose_name='Pick_Up')),
                ('drop_off', models.CharField(db_column='drop_off', max_length=50, verbose_name='Drop_Off')),
                ('email', models.EmailField(db_column='email', max_length=50, verbose_name='Email')),
                ('phone', models.CharField(db_column='phone', max_length=50, verbose_name='Phone')),
            ],
            options={
                'db_table': 'booking_car_details',
            },
        ),
        migrations.CreateModel(
            name='CruisesBooking',
            fields=[
                ('cruises_booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('agency_id', models.IntegerField(blank=True, null=True)),
                ('addres', models.CharField(db_column='addres', max_length=50, verbose_name='Addres')),
                ('check_in', models.DateField(db_column='check_in', max_length=50, verbose_name='Check_in')),
                ('check_out', models.DateField(db_column='check_out', max_length=50, verbose_name='Check_Out')),
                ('passport', models.CharField(db_column='passport', max_length=50, verbose_name='Passport')),
                ('select_class', models.CharField(db_column='select_class', max_length=50, verbose_name='Select_Class')),
                ('no_adults', models.CharField(db_column='no_adults', max_length=50, verbose_name='No_Adults')),
                ('no_children', models.CharField(db_column='no_children', max_length=50, verbose_name='No_Children')),
                ('email', models.EmailField(db_column='email', max_length=50, verbose_name='Email')),
                ('phone', models.CharField(db_column='phone', max_length=50, verbose_name='Phone')),
            ],
            options={
                'db_table': 'booking_cruises_details',
            },
        ),
        migrations.CreateModel(
            name='FlightBooking',
            fields=[
                ('flight_booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('agency_id', models.IntegerField(blank=True, null=True)),
                ('addres', models.CharField(db_column='addres', max_length=50, verbose_name='Addres')),
                ('check_in', models.DateField(db_column='check_in', max_length=50, verbose_name='Check_in')),
                ('check_out', models.DateField(db_column='check_out', max_length=50, verbose_name='Check_Out')),
                ('passport', models.CharField(db_column='passport', max_length=50, verbose_name='Passport')),
                ('select_class', models.CharField(db_column='select_class', max_length=50, verbose_name='Select_Class')),
                ('no_adults', models.CharField(db_column='no_adults', max_length=50, verbose_name='No_Adults')),
                ('no_children', models.CharField(db_column='no_children', max_length=50, verbose_name='No_Children')),
                ('email', models.EmailField(db_column='email', max_length=50, verbose_name='Email')),
                ('phone', models.CharField(db_column='phone', max_length=50, verbose_name='Phone')),
            ],
            options={
                'db_table': 'booking_flight_details',
            },
        ),
        migrations.CreateModel(
            name='RoomBooking',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('room_id', models.IntegerField(blank=True, null=True)),
                ('room_addres', models.CharField(db_column='room_Addres', max_length=50, verbose_name='Room_Addres')),
                ('room_check_in', models.DateField(db_column='room_check_in', max_length=50, verbose_name='Room_Check_In')),
                ('room_check_out', models.DateField(db_column='room_check_out', max_length=50, verbose_name='Room_Check_Out')),
                ('no_room', models.CharField(db_column='no_rooms', max_length=50, verbose_name='No_Rooms')),
                ('no_adults', models.CharField(db_column='no_adults', max_length=50, verbose_name='No_Adults')),
                ('no_children', models.CharField(db_column='no_children', max_length=50, verbose_name='No_Children')),
                ('email', models.EmailField(db_column='email', max_length=50, verbose_name='Email')),
                ('phone', models.CharField(db_column='phone', max_length=50, verbose_name='Phone')),
            ],
            options={
                'db_table': 'booking_room_details',
            },
        ),
        migrations.CreateModel(
            name='UserFb',
            fields=[
                ('fb_id', models.AutoField(primary_key=True, serialize=False)),
                ('rating', models.CharField(db_column='rating', max_length=50, verbose_name='Rating')),
                ('hotel_id', models.CharField(db_column='hotel_id', max_length=50, null=True, verbose_name='Hotel_id')),
                ('comments', models.TextField(db_column='comments', max_length=50, verbose_name='Comments')),
                ('agency_id', models.CharField(db_column='agency_id', max_length=50, verbose_name='Agency_id')),
            ],
            options={
                'db_table': 'user_fb',
            },
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.TextField(db_column='user_name', max_length=50, verbose_name='User_Name')),
                ('user_lastname', models.TextField(db_column='user_lastname', max_length=50, verbose_name='User_lastname')),
                ('user_phone', models.BigIntegerField(db_column='user_phone', verbose_name='User_Phone')),
                ('user_email', models.EmailField(blank=True, db_column='user_email', max_length=100, null=True, verbose_name='User_Email')),
                ('user_pwd', models.CharField(db_column='user_pwd', max_length=100, verbose_name='User_Password')),
                ('user_photo', models.ImageField(db_column='user_photo', null=True, upload_to='user/images/', verbose_name='User_Photo')),
            ],
            options={
                'db_table': 'user_details',
            },
        ),
    ]
