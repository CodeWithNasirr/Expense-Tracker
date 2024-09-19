from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.Tracker,name='Tracker'),
    path('Delete/<int:id>',views.Delete,name="Deleted"),
    path('crop-image/', views.crop_image_page, name='crop_image_page'),
    # path('upload-cropped-image/', views.upload_cropped_image, name='upload_cropped_image'),
]