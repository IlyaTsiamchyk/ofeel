from django.db import models

# Create your models here.
class Type(models.Model): #vegan
    name = models.CharField(max_length=200)


class Category(models.Model):
    name = models.CharField(max_length=200)
    type = models.ManyToManyField(Type)

    def __str__(self):
        return "Category" + self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Dish(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    class Meta:
        db_table = "DIshes"



class Product(models.Model):
    name = models.CharField(max_length=200)
    proteinsNumber = models.IntegerField() #gramm
    lipidsNumber = models.IntegerField() #gramm
    energyValue = models.IntegerField() #kal
    cost = models.DecimalField(decimal_places=4, max_digits=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)