from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, upload_to=name)

    def __str__(self):
        return '{}'.format(self.name)


class PokemonEntity(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    appeared_at = models.DateTimeField(null=True)
    disappeared_at = models.DateTimeField(null=True)
    level = models.IntegerField()
    health = models.IntegerField()
    strength = models.IntegerField()
    defence = models.IntegerField()
    stamina = models.IntegerField()

    def __str__(self):
        return 'lat: {}, lon: {}'.format(self.lat, self.lon)