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

@receiver(post_save,sender=UserProfile)
def create_thub(sender,instance , created , **kwargs):
    print(instance.avatar.name)
    if created:
        sizes = {
            'thumbnail_small':(100,100),
            'thumbnail_medium':(300,300),
            'thumbnail_large':(600,600),
        }

    for fields, size in sizes.items(): 
        img = Image.open(instance.avatar.path)
        img.thumbnail(size, Image.Resampling.LANCZOS)
        if img.mode=='RGBA':
            img=img.convert('RGB')
        # Get the base name and extension correctly
        file_name,file_exten=os.path.splitext(os.path.basename(instance.avatar.name))
        # print(file_exten)  # This will print something like '.jpg'
        # print(file_name)       # This will print the base file name like 'example'

        # Create the new file name for the thumbnail
        thub_fileName = f"{file_name}_{size[0]}X{size[1]}{file_exten}"
        thub_path = f"thubnails/{thub_fileName}"

        # Save the thumbnail
        img.save(os.path.join(os.path.dirname(instance.avatar.path), thub_path))
        print(os.path.join(os.path.dirname(instance.avatar.path), thub_path))

        # Update the respective field in the model instance
        setattr(instance, fields, thub_path)
class Register(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
