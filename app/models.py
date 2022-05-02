from django.db import models

# Create your models here.
class Cels(models.Model):
    modelo = models.CharField(max_length=150)
    marca = models.CharField(max_length=100)
    preco = models.FloatField()