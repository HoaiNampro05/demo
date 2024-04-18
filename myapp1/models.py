from django.db import models

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=100)
    link_img = models.CharField(max_length=200)