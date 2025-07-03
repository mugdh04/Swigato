from django.db import models
import datetime
# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    image = models.ImageField(upload_to='media/')

class MenuItem(models.Model):
    item_id = models.CharField(unique = 'True',max_length=8)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='media/')
    rating = models.FloatField()

class Contact_Query(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    message = models.CharField(max_length=400)
    date_time = models.DateTimeField(("Date"), default=datetime.datetime.today)
    def __str__(self):
        return self.email

class Product(models.Model):
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    description = models.TextField()
    calories = models.IntegerField()
    protein = models.FloatField()
    carbs = models.FloatField()
    fats = models.FloatField()
    fiber = models.FloatField()
    price = models.IntegerField()
    rating = models.FloatField()

    def __str__(self):
        return f"{self.name}"