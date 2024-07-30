from django.contrib import admin

# Register your models here.
from .models import (
    Brand, Product, MachineBrand, UserKYC,  Crop, Payment,
    Machine, Category, SubCategory, Field, CropUnit, MachineBooking, UserCompany
)

admin.site.site_header = "Farmer's Portal"
admin.site.site_title = "Farmer's Portal"
admin.site.index_title = "Farmer's Portal"


# Register your models here.
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(MachineBrand)
admin.site.register(UserKYC)
# admin.site.register(CustomUser)
admin.site.register(Crop)
admin.site.register(Payment)
admin.site.register(Machine)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Field)
admin.site.register(CropUnit)
admin.site.register(MachineBooking)
admin.site.register(UserCompany)