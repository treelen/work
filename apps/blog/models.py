from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(
        max_length=20
    )
    logo=models.ImageField(
        upload_to='logo/'
    )
    description=models.TextField(
        max_length=200
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'блок'
        verbose_name_plural = 'блоки'
    