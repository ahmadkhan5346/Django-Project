from django.contrib import admin

# Register your models here.

from .models import Product
from shop.models import Contact
from shop.models import Order, OrderUpdate

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(OrderUpdate)
