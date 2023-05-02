from django.db import models

# Create your models here.
class Contact(models.Model):
    phone_number = models.CharField(
        max_length=50
    )
    email = models.EmailField(
        max_length=254
    )
    locate = models.CharField(
        max_length=50
    )
    locate_url=models.URLField(
       
    )
    facebook_url=models.URLField(
       
    )
    instagram_url=models.URLField(
       
    )
    youtube_url=models.URLField(
       
    )