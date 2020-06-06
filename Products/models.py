from django.db import models

# Create your models here.

class Products(models.Model):
    prod_no = models.IntegerField()
    prod_name = models.CharField(max_length = 50)
    prod_price = models.FloatField()
    prod_qty = models.IntegerField()

    
