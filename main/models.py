from django.db import models

# Create your models here.

class Sepatu(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
