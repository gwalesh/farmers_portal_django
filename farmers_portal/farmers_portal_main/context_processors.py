from .models import Product
from .models import MachineBrand
from .models import Crop 
from .models import Machine 
from .models import Category
from .models import SubCategory
from .models import Field
from .models import MachineBooking

def access_setting(request):
    all_product = Product.objects.all()
    all_machinebrand    = MachineBrand.objects.all()
    all_crop = Crop.objects.all()
    all_machine = Machine.objects.all()
    all_category = Category.objects.all()
    all_subcategory = SubCategory.objects.all()
    all_field = Field.objects.all()
    all_machinebooking = MachineBooking.objects.all()
    return {'Products': all_product, 'MachineBrands': all_machinebrand, 'Crops': all_crop,
            'Machines': all_machine, 'Category': all_category, 'Subcategory': all_subcategory,
            'Fields': all_field, 'MachineBookings': all_machinebooking}