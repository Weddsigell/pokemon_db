from django.db import models


class Pockemon(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, upload_to=name)

    def __str__(self):
        return '{}'.format(self.name)
