# Generated by Django 3.2.8 on 2022-03-18 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0011_auto_20220315_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelmodel',
            name='status',
            field=models.CharField(default='pending', max_length=100, null=True),
        ),
    ]