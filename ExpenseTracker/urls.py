"""
URL configuration for ExpenseTracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Tracker import views as T_views

from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.shortcuts import render,redirect
from django.conf import settings
from django.conf.urls.static import static

def custum_logout(request):
    logout(request)
    return redirect('logout_success')
urlpatterns = [
    path('',include('Tracker.urls')),
    path('admin/', admin.site.urls),
    path('register',T_views.Register,name='Register'),
    path('login',auth_views.LoginView.as_view(template_name='tracker/login.html'),name='login'),
    path('logout',custum_logout,name='logout'),
    path('logout-success/', auth_views.TemplateView.as_view(template_name='tracker/logout.html'), name='logout_success'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
