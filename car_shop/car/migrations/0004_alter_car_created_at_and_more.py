# Generated by Django 4.0.2 on 2022-02-09 15:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_alter_car_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 2, 9, 15, 17, 16, 274261)),
        ),
        migrations.AlterField(
            model_name='carmanufacturer',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 2, 9, 15, 17, 16, 274261)),
        ),
    ]
