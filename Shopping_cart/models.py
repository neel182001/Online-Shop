from django.db import models

# Create your models here.

class Shopping_cart(models.Model):
    cus_no = models.IntegerField()
    cus_name = models.CharField(max_length = 100)
    prod_no = models.IntegerField()
    prod_name = models.CharField(max_length = 50)
    
