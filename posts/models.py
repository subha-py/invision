from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.TextField()
    price = models.IntegerField()
    latitude = models.CharField(max_length=120)
    longitude = models.CharField(max_length=120)
    make_offer = models.BooleanField()

class Photo(models.Model):
    name = models.CharField(max_length=120)
    size = models.IntegerField()
    post = models.ForeignKey(to=Post,on_delete=models.CASCADE,related_name='photos')
    