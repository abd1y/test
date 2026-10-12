from django.urls import path
from .views import test,get_images
urlpatterns = [
    path('test/',test),
    path("imageTest/",get_images)
]