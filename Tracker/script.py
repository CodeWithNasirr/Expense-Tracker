from django.db.models import Sum
from .models import *
def tracker_total_cal():
    price=Transactions.objects.all().aggregate(total_sum=Sum('price'))
    return price

def tracker_Plus_cal():
    price=Transactions.objects.filter(price__gte=1).aggregate(total_sum=Sum('price'))
    return price

def tracker_minu_cal():
    price=Transactions.objects.filter(price__lte=1).aggregate(total_sum=Sum('price'))
    return price