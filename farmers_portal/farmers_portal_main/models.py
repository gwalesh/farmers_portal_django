from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Brand(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    thumbnail = models.ImageField(upload_to='brands/thumbnails/')

class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    available_quantity = models.IntegerField()
    units = models.CharField(max_length=255)
    mrp = models.BigIntegerField()
    selling_price = models.BigIntegerField()
    msp = models.BigIntegerField()
    bulk_price = models.BigIntegerField()
    bulk_quantity = models.BigIntegerField()
    thumbnail = models.ImageField(upload_to='products/thumbnails/')
    expiry_date = models.DateTimeField()
    shelf_life = models.BigIntegerField()
    barcode = models.CharField(max_length=255)
    uuid = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    subcategory = models.ForeignKey('SubCategory', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

class MachineBrand(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    thumbnail = models.ImageField(upload_to='machine_brands/thumbnails/')

class UserKYC(models.Model):
    user_id = models.CharField(max_length=255, primary_key=True)
    adhaar_no = models.BigIntegerField(unique=True)
    pan = models.CharField(max_length=255, unique=True)
    bank_name = models.CharField(max_length=255)
    ifsc_code = models.BigIntegerField()
    bank_account_number = models.BigIntegerField()
    is_verified = models.BooleanField(default=False)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.BigIntegerField(unique=True)
    is_verified = models.BooleanField(default=False)
    kyc_done = models.BooleanField(default=False)
    user_type = models.CharField(max_length=255, default='user')
    avatar = models.ImageField(upload_to='users/avatars/')
    uuid = models.CharField(max_length=255, unique=True)

class Crop(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='crops/images/')
    gallery = models.JSONField()
    quantity = models.IntegerField()
    unit = models.ForeignKey('CropUnit', on_delete=models.CASCADE)
    available_on = models.DateField()
    location = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)

class Payment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=255)
    payment_gateway = models.CharField(max_length=255)
    token_id = models.CharField(max_length=255, null=True, blank=True, unique=True)
    bank = models.CharField(max_length=255)
    wallet = models.CharField(max_length=255)
    upi_id = models.CharField(max_length=255)
    card_id = models.CharField(max_length=255, unique=True)
    contact = models.CharField(max_length=255)
    customer_id = models.CharField(max_length=255)

class Machine(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(MachineBrand, on_delete=models.CASCADE)
    model_number = models.IntegerField()

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='categories/thumbnails/')

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.CharField(max_length=255)

class Field(models.Model):
    farmer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    full_address = models.TextField()
    size = models.IntegerField()
    length = models.BigIntegerField()
    breadth = models.BigIntegerField()

class CropUnit(models.Model):
    unit = models.CharField(max_length=255)
    description = models.BigIntegerField()

class MachineBooking(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    farmer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='farmer')
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='owner')
    booked_from = models.DateTimeField()
    booked_to = models.DateTimeField()
    price_per_hour = models.FloatField()
    is_booking_confirmed = models.BooleanField()
    is_driver_confirmed = models.BooleanField()
    driver_assigned = models.IntegerField()
    trip_started = models.BooleanField()
    trip_started_at = models.DateTimeField()
    driver_reached = models.BooleanField()
    driver_reached_at = models.DateTimeField()
    time_taken = models.TimeField()
    selfie = models.ImageField(upload_to='machine_bookings/selfies/')

class UserCompany(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    reg_name = models.CharField(max_length=255)
    gstin = models.CharField(max_length=255)
    reg_add = models.CharField(max_length=255)
    udyam_reg_no = models.CharField(max_length=255, null=True, blank=True)
