from django.db import models


class ProhibitedGood(models.Model):
    product = models.CharField(max_length=100)
    replace = models.CharField(max_length=100)
    info = models.CharField(max_length=100)
