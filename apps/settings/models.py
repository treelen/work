from django.db import models

# Create your models here.
class Settings(models.Model):
    title=models.CharField(
        max_length=20
    )
    logo=models.ImageField(
        upload_to='logo/'
    )
    description=models.TextField(
        max_length=200
    )
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name='настройка'
        verbose_name_plural='настройки'
        