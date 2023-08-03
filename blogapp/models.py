from django.db import models
from datetime import date

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    image1 = models.ImageField(upload_to='images')
    image2 = models.ImageField(upload_to='images')
    image3 = models.ImageField(upload_to='images')
    quote = models.CharField(max_length=150,default="")
    description = models.TextField(default='It was a good day')
    def __str__(self):
        return self.title
