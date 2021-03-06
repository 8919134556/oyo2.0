# Generated by Django 3.2.8 on 2022-03-10 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_cardashboardmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='CruisesdashboardModel',
            fields=[
                ('cruises_id', models.AutoField(primary_key=True, serialize=False)),
                ('cruises_name', models.CharField(db_column='cruises_name', max_length=50, verbose_name='Cruises_name')),
                ('cruises_no', models.CharField(db_column='cruises_no', max_length=50, verbose_name='Cruises_no')),
                ('select_class', models.CharField(db_column='select_class', max_length=50, verbose_name='Select_class')),
                ('cruises_from', models.CharField(db_column='from', max_length=50, verbose_name='From')),
                ('to', models.CharField(db_column='to', max_length=50, verbose_name='To')),
                ('via', models.CharField(db_column='via', max_length=50, verbose_name='Via')),
                ('date', models.CharField(db_column='date', max_length=50, verbose_name='Date')),
                ('check_in', models.CharField(db_column='check_in', max_length=50, verbose_name='Check_in')),
                ('check_out', models.CharField(db_column='check_out', max_length=50, verbose_name='Check_out')),
                ('price', models.CharField(blank=True, db_column='price', max_length=100, null=True, verbose_name='Price')),
                ('cruises_photo', models.ImageField(db_column='cruises_photo', upload_to='room/images/', verbose_name='Cruises_photo')),
            ],
            options={
                'db_table': 'cruises_dashboard',
            },
        ),
        migrations.CreateModel(
            name='FlightdashboardModel',
            fields=[
                ('flight_id', models.AutoField(primary_key=True, serialize=False)),
                ('flight_name', models.CharField(db_column='flight_name', max_length=50, verbose_name='Flight_name')),
                ('flight_no', models.CharField(db_column='flight_no', max_length=50, verbose_name='Flight_no')),
                ('select_class', models.CharField(db_column='select_class', max_length=50, verbose_name='Select_class')),
                ('flight_from', models.CharField(db_column='trom', max_length=50, verbose_name='From')),
                ('to', models.CharField(db_column='to', max_length=50, verbose_name='To')),
                ('via', models.CharField(db_column='via', max_length=50, verbose_name='Via')),
                ('date', models.CharField(db_column='date', max_length=50, verbose_name='Date')),
                ('check_in', models.CharField(db_column='check_in', max_length=50, verbose_name='Check_in')),
                ('check_out', models.CharField(db_column='check_out', max_length=50, verbose_name='Check_out')),
                ('price', models.CharField(blank=True, db_column='price', max_length=100, null=True, verbose_name='Price')),
                ('flight_photo', models.ImageField(db_column='flight_photo', upload_to='room/images/', verbose_name='Flight_photo')),
            ],
            options={
                'db_table': 'flight_dashboard',
            },
        ),
    ]
