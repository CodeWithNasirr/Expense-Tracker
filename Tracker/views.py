from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
from Tracker.script import *
import os
from django.conf import settings
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def Tracker(request):
    if request.method == 'POST':
        # first you have to do make a FILES request to get the Image and save the Image which you get from the FILES-Request in a variable like(image),then also you use TRY exceptions for better view then you have check the which user send the FILES-Request How To Check? use xyz.objects.get(user=request.user) if it True then use if condition to check the image or avatar already in the DB or not if it True then find his exacat path if you find the path then remove it and when the if conditions is False means not avatar in DB then you have to Save the image From the DB! in the firstly you have you Try Exceptions if the Try is not True Means The (objects.get) is not founded or xyzx.Doesnotexist then create a new user with avatar and save it .... 
        if 'image' in request.FILES:
            image=request.FILES['image']
            # Try isliye laga rahe ha first checkhoga ki ye jo image upload hoga isse pahle koi or image exist() karta ha v ya nhi ager karta hoga to usko remove karenge then ye wala models pe save karenge
            try:
                user_profile=UserProfile.objects.get(user=request.user)
                if user_profile.avatar:
                    # old_img_path=os.path.join(settings.MEDIA_ROOT,str(user_profile.avatar))
                    old_img_path=user_profile.avatar.path
                    if os.path.exists(old_img_path):
                        try:
                            os.remove(old_img_path)
                        except FileNotFoundError:
                            print(f"File {old_img_path} Not Found Skip Deletions....")
                user_profile.avatar=image
                user_profile.save()

            except UserProfile.DoesNotExist:
                user_profile=UserProfile(user=request.user,avatar=image)
                user_profile.save()



        desc=request.POST.get('text')
        amount=request.POST.get('amount')
        if not desc:
            messages.info(request, 'Please Fill The Description')
            return redirect('/')
        if not amount:
            messages.info(request, 'Please Fill The Correct Price')
            return redirect('/')
        
        x=Transactions(user=request.user,desc=desc,price=float(amount))
        x.save()
        return redirect('/')
    value = {"Transactions":Transactions.objects.filter(user=request.user),"Total_Price":tracker_total_cal(request)['total_sum'],"Plus_Total":tracker_Plus_cal(request)["total_sum"],"Minus_Total":tracker_minu_cal(request)['total_sum'],'images':UserProfile.objects.filter(user=request.user)}
    return render(request,"tracker/index.html",value)

def Delete(request,id):
    Transactions.objects.filter(id=id).delete()
    return redirect('/')


def Register(request):
    if request.method =="POST":
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        pass2=request.POST.get('Confirm-password')
        if pass1 == pass2:
            if not username:
                messages.error(request, "Username is required.")
            elif pass1 != pass2:
                messages.error(request, "Password Do Not Match!")
            elif User.objects.filter(username=username).exists():
                messages.error(request,"Username is Already Exist! ")
            else:
                user=User.objects.create_user(username)
                user.set_password(pass1)
                user.save()
                messages.success(request,"Your account has been created succecfully ")
        else:
            messages.error(request,"Password Not Match! ")
    return render(request,'tracker/register.html')