# Generated by Django 3.2.8 on 2022-03-15 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0006_alter_cruisesdashboardmodel_cruises_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cruisesdashboardmodel',
            name='check_in',
            field=models.TimeField(db_column='check_in', max_length=50, verbose_name='Check_in'),
        ),
        migrations.AlterField(
            model_name='cruisesdashboardmodel',
            name='check_out',
            field=models.TimeField(db_column='check_out', max_length=50, verbose_name='Check_out'),
        ),
        migrations.AlterField(
            model_name='cruisesdashboardmodel',
            name='cruises_name',
            field=models.TextField(db_column='cruises_name', max_length=50, verbose_name='Cruises_name'),
        ),
        migrations.AlterField(
            model_name='cruisesdashboardmodel',
            name='date',
            field=models.DateField(db_column='date', max_length=50, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='flightdashboardmodel',
            name='check_in',
            field=models.TimeField(db_column='check_in', max_length=50, verbose_name='Check_in'),
        ),
        migrations.AlterField(
            model_name='flightdashboardmodel',
            name='check_out',
            field=models.TimeField(db_column='check_out', max_length=50, verbose_name='Check_out'),
        ),
        migrations.AlterField(
            model_name='flightdashboardmodel',
            name='date',
            field=models.DateField(db_column='date', max_length=50, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='travelmodel',
            name='agency_email',
            field=models.EmailField(blank=True, db_column='agency_email', max_length=100, null=True, verbose_name='Agency_Email'),
        ),
        migrations.AlterField(
            model_name='travelmodel',
            name='agency_name',
            field=models.TextField(db_column='agency_name', max_length=50, verbose_name='Agency_Name'),
        ),
        migrations.AlterField(
            model_name='travelmodel',
            name='agency_phone',
            field=models.BigIntegerField(db_column='agency_phone', max_length=50, verbose_name='Agency_Phone'),
        ),
    ]
