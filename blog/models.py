from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    img=  models.ImageField(upload_to='product/')
    price = models.IntegerField()


    def __str__(self):
        return self.name


class About(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    img = models.ImageField(upload_to='about/')
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Carusel(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    img = models.ImageField(upload_to='carusel/')
    price = models.IntegerField()


    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    img = models.ImageField(upload_to='customer/')
    price = models.IntegerField()

    def __str__(self):
        return self.name


