# Generated by Django 3.2.8 on 2022-03-10 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0003_cruisesdashboardmodel_flightdashboardmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardashboardmodel',
            name='car_photo',
            field=models.ImageField(db_column='car_photo', upload_to='car/images/', verbose_name='Car_photo'),
        ),
    ]
