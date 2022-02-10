# Generated by Django 4.0.2 on 2022-02-10 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('car', '0001_initial'),
        ('showroom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountSupplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('discount_percent', models.DecimalField(decimal_places=2, max_digits=4)),
                ('disc_start', models.DateField(auto_now_add=True, verbose_name='Discount start at')),
                ('disc_end', models.DateField(auto_now_add=True, verbose_name='Discount end at')),
                ('cars', models.ManyToManyField(to='car.Car')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Supplier name')),
                ('foundation', models.DateField(blank=True, default=2022, verbose_name='Foundation date')),
                ('cars', models.ManyToManyField(blank=True, null=True, to='car.Car')),
                ('current_discount', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='discount', to='supplier.discountsupplier')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SupplierHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=100, verbose_name='Price')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.car')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplier.supplier')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='supplier',
            name='sale_history',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='history', to='supplier.supplierhistory'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='showrooms',
            field=models.ManyToManyField(blank=True, null=True, related_name='showrooms', to='showroom.Showroom'),
        ),
        migrations.AddField(
            model_name='discountsupplier',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplier.supplier'),
        ),
    ]
