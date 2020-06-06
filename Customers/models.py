from django.db import models

# Create your models here.

class Customers(models.Model):
    cus_no = models.IntegerField()
    cus_name = models.CharField(max_length = 100)
    cus_addr = models.CharField(max_length = 500)
    cus_phno = models.CharField(max_length = 10)
    
