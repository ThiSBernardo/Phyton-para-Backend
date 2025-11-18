from django.db import models

# Create your models here.
class Product(models.Model):
    titulo = models.CharField(max_length=150)
    preco = models.DecimalField(max_digits=10, decimal_places=2)