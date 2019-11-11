from django.db import models

# Create your models here.


class Nojapan(models.Model):

    product = models.CharField(max_length=100)
    replace = models.CharField(max_length=100)
    info = models.CharField(max_length=100)
