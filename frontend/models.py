from django.db import models

# Create your models here.



class Electronics(models.Model):
    Name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to='images/electronics')
    description = models.TextField(max_length= 40)

    def __str__(self):
        return self.Name


class Clothing(models.Model):
    Name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to='images/clothing')
    description = models.TextField(max_length= 40)

    def __str__(self):
        return self.Name


class  Furniture(models.Model):
    Name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to='images/furniture')
    description = models.TextField(max_length= 40)

    def __str__(self):
        return self.Name

