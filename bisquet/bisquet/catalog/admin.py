from django.contrib import admin

from .models import Product, Unit, Category

admin.site.register(Product)
admin.site.register(Unit)
admin.site.register(Category)
