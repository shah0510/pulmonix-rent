from django.contrib import admin

from .models import Product_name, Items, Technician, Product_code


admin.site.register(Product_name)
admin.site.register(Items)
admin.site.register(Technician)
admin.site.register(Product_code)