from django.db.models import Sum
from .models import *
def tracker_total_cal(request):
    price=Transactions.objects.filter(user=request.user).aggregate(total_sum=Sum('price'))
    return price

def tracker_Plus_cal(request):
    price=Transactions.objects.filter(user=request.user,price__gte=1).aggregate(total_sum=Sum('price'))
    return price

def tracker_minu_cal(request):
    price=Transactions.objects.filter(user=request.user,price__lte=1).aggregate(total_sum=Sum('price'))
    return price