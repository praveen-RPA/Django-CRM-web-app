from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=50,null=True)
    phone=models.IntegerField(null=True)
    email=models.EmailField(max_length=50,null=True)
    date_created=models.DateTimeField(auto_now_add=True)

    #instead of seeing customer(1) in DB we use name
    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=50,null=True)

    #instead of seeing customer(1) in DB we use name
    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY=(
        ('indoor','indoor'),
        ('out door','out door'),
    )
    name=models.CharField(max_length=50,null=True)
    price=models.FloatField(null=True)
    category=models.CharField(max_length=50,null=True,choices=CATEGORY)
    description=models.TextField(max_length=50,null=True, blank=True)
    date_created=models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag)

    #if we are not using it will represent the product object(1) ,if we use -BBq (product name will display)
    def __str__(self):
        return self.name



class Order(models.Model):
    STATUS=(
        ('pending','pending'),
        ('out for delivery','out for delivery'),
        ('Delivered','Delivered'),
    )
    #one to many relationship - every time customer ask some product we don't want manually add price and name
    #on_delete=models.SET_NULL - if sometime customer deleted it have a data of what customer purchased
    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)
    def __str__(self):
        return self.product.name

