from django.db import models

# Create your models here.

class Transactions(models.Model):
    desc=models.CharField(max_length=100)
    price=models.FloatField(default='$0.00')