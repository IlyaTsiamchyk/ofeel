from django.db import models

# Create your models here.
class FoodType(models.Model): #vegan
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class FoodCategory(models.Model): #steamed, fried, boiled
    name = models.CharField(max_length=200)
    food_type = models.ManyToManyField(FoodType)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Food category"
        verbose_name_plural = "Food categories"


class Product(models.Model):
    name = models.CharField(max_length=200)
    proteinsNumber = models.IntegerField() #gramm
    lipidsNumber = models.IntegerField() #gramm
    energyValue = models.IntegerField() #kal
    cost = models.DecimalField(decimal_places=4, max_digits=100)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=200)
    food_category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Ofeel_Dishes"

    class Meta:
        verbose_name = "Dish"
        verbose_name_plural = "Dishes"
