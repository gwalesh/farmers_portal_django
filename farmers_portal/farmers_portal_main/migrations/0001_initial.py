# Generated by Django 4.2.14 on 2024-07-30 03:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('thumbnail', models.ImageField(upload_to='brands/thumbnails/')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='categories/thumbnails/')),
            ],
        ),
        migrations.CreateModel(
            name='CropUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=255)),
                ('description', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('model_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MachineBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('thumbnail', models.ImageField(upload_to='machine_brands/thumbnails/')),
            ],
        ),
        migrations.CreateModel(
            name='UserKYC',
            fields=[
                ('user_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('adhaar_no', models.BigIntegerField(unique=True)),
                ('pan', models.CharField(max_length=255, unique=True)),
                ('bank_name', models.CharField(max_length=255)),
                ('ifsc_code', models.BigIntegerField()),
                ('bank_account_number', models.BigIntegerField()),
                ('is_verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.BigIntegerField(unique=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('kyc_done', models.BooleanField(default=False)),
                ('user_type', models.CharField(default='user', max_length=255)),
                ('avatar', models.ImageField(upload_to='users/avatars/')),
                ('uuid', models.CharField(max_length=255, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_name', models.CharField(max_length=255)),
                ('gstin', models.CharField(max_length=255)),
                ('reg_add', models.CharField(max_length=255)),
                ('udyam_reg_no', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmers_portal_main.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('description', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmers_portal_main.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('available_quantity', models.IntegerField()),
                ('units', models.CharField(max_length=255)),
                ('mrp', models.BigIntegerField()),
                ('selling_price', models.BigIntegerField()),
                ('msp', models.BigIntegerField()),
                ('bulk_price', models.BigIntegerField()),
                ('bulk_quantity', models.BigIntegerField()),
                ('thumbnail', models.ImageField(upload_to='products/thumbnails/')),
                ('expiry_date', models.DateTimeField()),
                ('shelf_life', models.BigIntegerField()),
                ('barcode', models.CharField(max_length=255)),
                ('uuid', models.CharField(max_length=255, unique=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmers_portal_main.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmers_portal_main.category')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmers_portal_main.subcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(max_length=255)),
                ('payment_gateway', models.CharField(max_length=255)),
                ('token_id', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('bank', models.CharField(max_length=255)),
                ('wallet', models.CharField(max_length=255)),
                ('upi_id', models.CharField(max_length=255)),
                ('card_id', models.CharField(max_length=255, unique=True)),
                ('contact', models.CharField(max_length=255)),
                ('customer_id', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmers_portal_main.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='MachineBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked_from', models.DateTimeField()),
                ('booked_to', models.DateTimeField()),
                ('price_per_hour', models.FloatField()),
                ('is_booking_confirmed', models.BooleanField()),
                ('is_driver_confirmed', models.BooleanField()),
                ('driver_assigned', models.IntegerField()),
                ('trip_started', models.BooleanField()),
                ('trip_started_at', models.DateTimeField()),
                ('driver_reached', models.BooleanField()),
                ('driver_reached_at', models.DateTimeField()),
                ('time_taken', models.TimeField()),
                ('selfie', models.ImageField(upload_to='machine_bookings/selfies/')),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='farmer', to='farmers_portal_main.userprofile')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmers_portal_main.machine')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='farmers_portal_main.userprofile')),
            ],
        ),
        migrations.AddField(
            model_name='machine',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmers_portal_main.machinebrand'),
        ),
        migrations.AddField(
            model_name='machine',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmers_portal_main.userprofile'),
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('full_address', models.TextField()),
                ('size', models.IntegerField()),
                ('length', models.BigIntegerField()),
                ('breadth', models.BigIntegerField()),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmers_portal_main.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('image', models.ImageField(upload_to='crops/images/')),
                ('gallery', models.JSONField()),
                ('quantity', models.IntegerField()),
                ('available_on', models.DateField()),
                ('location', models.CharField(max_length=255)),
                ('latitude', models.CharField(max_length=255)),
                ('longitude', models.CharField(max_length=255)),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmers_portal_main.cropunit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmers_portal_main.userprofile')),
            ],
        ),
    ]
