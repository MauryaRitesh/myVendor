from django.contrib import admin

# Register your models here.
from .models import Product
from .models import Orders

admin.site.register(Product)

admin.site.register(Orders)

