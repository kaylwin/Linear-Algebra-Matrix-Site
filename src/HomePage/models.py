from django.db import models


class user(models.Model):
    first_name = models.CharField(max_length=200)
    last_name  = models.DateTimeField('date published')

    
    