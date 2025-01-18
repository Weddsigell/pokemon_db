from django.db import models

class Pockemon(models.Model):
    name = models.CharField(max_length=100)
