from django.contrib import admin
from .models import Transactions,UserProfile,Register
# Register your models here.

admin.site.register(Transactions)
admin.site.register(UserProfile)
admin.site.register(Register)