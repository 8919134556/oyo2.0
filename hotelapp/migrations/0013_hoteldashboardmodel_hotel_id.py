# Generated by Django 3.2.8 on 2022-03-21 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0012_hotelmodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='hoteldashboardmodel',
            name='hotel_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]