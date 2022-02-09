# Generated by Django 4.0.2 on 2022-02-09 15:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('showroom', '0004_remove_showroom_updated_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='showroom',
            name='created_at',
        ),
        migrations.AddField(
            model_name='showroom',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 9, 15, 17, 58, 46958)),
        ),
        migrations.AlterField(
            model_name='discountshowroom',
            name='disc_end',
            field=models.DateField(default=datetime.datetime(2022, 2, 9, 15, 17, 58, 133496, tzinfo=utc), verbose_name='Discount end at'),
        ),
        migrations.AlterField(
            model_name='discountshowroom',
            name='disc_start',
            field=models.DateField(default=datetime.datetime(2022, 2, 9, 15, 17, 58, 133479, tzinfo=utc), verbose_name='Discount start at'),
        ),
        migrations.AlterField(
            model_name='showroomhistory',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 2, 9, 15, 17, 58, 46831)),
        ),
    ]