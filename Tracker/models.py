from django.db import models
from PIL import Image
from django.contrib.auth.models import User
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

    # def save(self, *args, **kwargs):
    #     super(UserProfile, self).save(*args, **kwargs)
    #     img = Image.open(self.avatar.path)

    #     if img.height > 180 or img.width > 180:
    #         output_size = (180, 180)
    #         img.thumbnail(output_size,Image.Resampling.LANCZOS)
    #         img.save(self.avatar.path)


class Register(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)