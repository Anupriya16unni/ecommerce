from django.db import models

from common.models import Customer, Reseller
from reseller.models import Product

# Create your models here.
class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(Customer,on_delete=models.CASCADE)

    class meta:
        db_table='cart'