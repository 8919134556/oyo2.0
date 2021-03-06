# Generated by Django 3.2.8 on 2022-03-04 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HotelModel',
            fields=[
                ('hotel_id', models.AutoField(primary_key=True, serialize=False)),
                ('hotel_name', models.CharField(db_column='hotel_name', max_length=50, verbose_name='Hotel_Name')),
                ('hotel_pan_number', models.CharField(db_column='hotel_pan_number', max_length=50, verbose_name='Hotel_Pan_number')),
                ('hotel_addres', models.CharField(db_column='hotel_Addres', max_length=50, verbose_name='Hotel_Addres')),
                ('hotel_phone', models.CharField(db_column='hotel_phone', max_length=50, verbose_name='Hotel_Phone')),
                ('hotel_email', models.CharField(blank=True, db_column='hotel_email', max_length=100, null=True, verbose_name='Hotel_Email')),
                ('hotel_pwd', models.CharField(db_column='hotel_pwd', max_length=100, verbose_name='Hotel_Password')),
                ('hotel_photo', models.ImageField(db_column='hotel_photo', upload_to='images/', verbose_name='Hotel_Photo')),
                ('hotel_certificate', models.ImageField(db_column='hotel_certificate', upload_to='images/', verbose_name='Hotel_Certificate')),
            ],
            options={
                'db_table': 'hotel_details',
            },
        ),
    ]
