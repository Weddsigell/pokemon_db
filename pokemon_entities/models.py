from django.db import models


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)
    title_jp = models.CharField(max_length=100)
    description = models.TextField()
    previous_evolutions = models.ForeignKey('self',
                                       null=True,
                                       blank=True,
                                       related_name='next_evolution',
                                       on_delete=models.SET_NULL)
    image = models.ImageField(null=True, upload_to=title_en, blank=True,)

    def __str__(self):
        return '{}'.format(self.title_en)


class PokemonEntity(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    appeared_at = models.DateTimeField(null=True)
    disappeared_at = models.DateTimeField(null=True)
    level = models.IntegerField(null=True)
    health = models.IntegerField(null=True)
    strength = models.IntegerField(null=True)
    defence = models.IntegerField(null=True)
    stamina = models.IntegerField(null=True)

    def __str__(self):
        return 'lat: {}, lon: {}'.format(self.lat, self.lon)