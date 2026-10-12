from django.db import models

# Create your models here.
from cloudinary.models import CloudinaryField

class testImage(models.Model):
    title=models.CharField(max_length=200)
    image=CloudinaryField("image")