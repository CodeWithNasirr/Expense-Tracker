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
    if instance.avatar:
        avatar_path=instance.avatar.path
        img=Image.open(avatar_path)
        max_size=(1000,1000)

        if img.height>max_size[0] or img.width>max_size[1]:
            img.thumbnail(max_size)
            img.save(avatar_path)
            print('Resizer Image Saved Succesfully')
class Register(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
