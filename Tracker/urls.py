from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.Tracker,name='Tracker'),
    path('Delete/<int:id>',views.Delete,name="Deleted"),
]