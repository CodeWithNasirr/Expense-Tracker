from django.db import models
from PIL import Image,ExifTags
from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save,post_delete,pre_delete
from django.dispatch import receiver
from django.utils import timezone
import os
from django.conf import settings
# Create your models here.

class Transactions(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    desc=models.CharField(max_length=100)
    price=models.FloatField(default='$0.00')

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    avatar = models.ImageField(upload_to='avatars/')
    uploaded_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self) -> str:
        return f"{self.user.id} - {self.user.username}"
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    avatar = models.ImageField(upload_to='avatars/')
    uploaded_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self) -> str:
        return f"{self.user.id} - {self.user.username}"

@receiver(post_save, sender=UserProfile)
def Avtar_Resizer(sender, instance, created, **kwargs):
    # sab se pahle avtar check karna ha wo db pe ha ya nhi if it true then save the path in variable just-like(avatar_path) and next open Image From this path when the image open means it  True then Reize it and save into the thumbnail and lastly when the img resize save into the same path if you save in the same path it acctully save the same data base path 
    if instance.avatar:
        avatar_path=instance.avatar.path
        img=Image.open(avatar_path)
        max_size=(1000,1000)

        if img.height>max_size[0] or img.width>max_size[1]:
            img.thumbnail(max_size)
            img.save(avatar_path)
            print('Resizer Image Saved Succesfully')
# After a User is created, automatically create a related UserProfile if it doesn’t exist.
@receiver(post_save,sender=User)
def create_or_update_user_profile(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()
# After a UserProfile is deleted, remove the avatar image file from the filesystem to free up
@receiver(post_delete,sender=UserProfile)
def delete_avatar(sender,instance,**kwargs):
    if instance.avatar:
        avatar_path=instance.avatar.path
        if os.path.exists(avatar_path):
            os.remove(avatar_path)
            print(f"Deleted Avatar: {avatar_path}")
from django.core.exceptions import ValidationError
@receiver(pre_delete,sender=Transactions)
def check_Transactons_dependencies(sender,instance,**kwargs):
    if Transactions.objects.filter(desc=instance).exists():
        raise ValidationError('Cannot delete desc asscoiated')
class Register(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
