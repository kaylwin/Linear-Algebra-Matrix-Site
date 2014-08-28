from django.db import models

# Create your models here.
class Matrix(models.Model):
    m = models.IntegerField();
    n = models.IntegerField();
