from django.db import models
from common.models import Reseller
# Create your models here.

class Product(models.Model):
    product_name=models.CharField(max_length=20)
    seller=models.ForeignKey(Reseller,on_delete=models.CASCADE)
    desc=models.CharField(max_length=100)
    price=models.FloatField()
    stock=models.IntegerField()
    image=models.ImageField(upload_to='product/')