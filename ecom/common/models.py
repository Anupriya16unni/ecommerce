import email
from unicodedata import name
from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    email=models.CharField(max_length=30)
    mobile_number=models.BigIntegerField()
    user_name=models.CharField(max_length=30)
    password=models.CharField(max_length=40)

    class Meta:
        db_table="customer"

class Reseller(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    mobile_number=models.BigIntegerField()
    adhar_number=models.BigIntegerField()
    holder_name=models.CharField(max_length=20)
    account_number=models.BigIntegerField()
    ifsc_code=models.CharField(max_length=30)
    user_name=models.CharField(max_length=30)
    password=models.CharField(max_length=40)

    class Meta:
        db_table="reseller"