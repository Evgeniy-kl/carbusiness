# Generated by Django 4.0.2 on 2022-02-09 15:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('showroom', '0003_showroom_created_at_alter_discountshowroom_disc_end_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='showroom',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='discountshowroom',
            name='disc_end',
            field=models.DateField(default=datetime.datetime(2022, 2, 9, 15, 17, 16, 359705, tzinfo=utc), verbose_name='Discount end at'),
        ),
        migrations.AlterField(
            model_name='discountshowroom',
            name='disc_start',
            field=models.DateField(default=datetime.datetime(2022, 2, 9, 15, 17, 16, 359687, tzinfo=utc), verbose_name='Discount start at'),
        ),
        migrations.AlterField(
            model_name='showroom',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 2, 9, 15, 17, 16, 274261)),
        ),
        migrations.AlterField(
            model_name='showroomhistory',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 2, 9, 15, 17, 16, 274261)),
        ),
    ]
