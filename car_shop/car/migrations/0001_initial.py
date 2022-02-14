# Generated by Django 4.0.2 on 2022-02-10 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarManufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Manufacturer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('model', models.CharField(max_length=100, unique=True, verbose_name='Car model')),
                ('features', models.JSONField()),
                ('description', models.TextField()),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manufacturer', related_query_name='manufacturers', to='car.carmanufacturer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
