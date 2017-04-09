from django.contrib import admin
from .models import Dish, Product, FoodCategory, FoodType

# Register your models here.

admin.site.register(Dish)
admin.site.register(Product)
admin.site.register(FoodCategory)
admin.site.register(FoodType)