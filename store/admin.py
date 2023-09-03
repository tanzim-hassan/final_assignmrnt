from django.contrib import admin
from . models import Car

# Register your models here.

class productAdmin(admin.ModelAdmin):
    list_display=['car_name','price','category','stck','category_date',
                  'modified_date','is_available']
    
    prepopulated_fields={'slug':('product_name',)}
admin.site.register(Car,productAdmin)