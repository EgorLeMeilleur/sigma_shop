from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import TShirt, Sweatshirt, Hoody, Product, ProductImage

admin.site.register(Product)
admin.site.register(TShirt)
admin.site.register(Sweatshirt)
admin.site.register(Hoody)
admin.site.register(ProductImage)

