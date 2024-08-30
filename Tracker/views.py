from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
from Tracker.script import *
# Create your views here.

def Tracker(request):
    if request.method == 'POST':
        desc=request.POST.get('text')
        amount=request.POST.get('amount')
        if not desc:
            messages.info(request, 'Please Fill The Description')
            return redirect('/')
        if not amount:
            messages.info(request, 'Please Fill The Correct Price')
            return redirect('/')
        
        x=Transactions(desc=desc,price=amount)
        x.save()
        return redirect('/')
    value = {"Transactions":Transactions.objects.all(),"Total_Price":tracker_total_cal()['total_sum'],"Plus_Total":tracker_Plus_cal()["total_sum"],"Minus_Total":tracker_minu_cal()['total_sum']}
    return render(request,"tracker/index.html",value)

def Delete(request,id):
    Transactions.objects.filter(id=id).delete()
    return redirect('/')