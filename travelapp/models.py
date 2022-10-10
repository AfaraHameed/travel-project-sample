from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='picture')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

class Post(models.Model):
    date = models.DateField()
    image = models.ImageField(upload_to='blog_picture')
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)



