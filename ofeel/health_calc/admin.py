from django.contrib import admin
from .models import Dish, Product, Category, Type

# Register your models here.

admin.site.register(Dish)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Type)