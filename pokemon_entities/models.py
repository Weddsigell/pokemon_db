from django.db import models


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=100, verbose_name='имя на русском')
    title_en = models.CharField(max_length=100, verbose_name='имя на английском', null=True, blank=True, )
    title_jp = models.CharField(max_length=100, verbose_name='имя на японском', null=True, blank=True, )
    description = models.TextField(verbose_name='описание покемона', null=True, blank=True, )
    previous_evolutions = models.ForeignKey(
        'self',
        verbose_name='следующая эволюция',
        null=True,
        blank=True,
        related_name='next_evolution',
        on_delete=models.SET_NULL
    )
    image = models.ImageField(verbose_name='картинка покемона', null=True, upload_to=title_en, blank=True,)

    def __str__(self):
        return '{}'.format(self.title_en)


class PokemonEntity(models.Model):
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    pokemon = models.ForeignKey(Pokemon, related_name="pokemon_entity", on_delete=models.CASCADE, verbose_name='Тип покемона')
    appeared_at = models.DateTimeField(null=True, verbose_name='когда появляется')
    disappeared_at = models.DateTimeField(null=True, verbose_name='когда пропадает')
    level = models.IntegerField(null=True, blank=True, verbose_name='уровень')
    health = models.IntegerField(null=True, blank=True, verbose_name='здоровье')
    strength = models.IntegerField(null=True, blank=True, verbose_name='сила')
    defence = models.IntegerField(null=True, blank=True, verbose_name='защита')
    stamina = models.IntegerField(null=True, blank=True, verbose_name='выносливость')

    def __str__(self):
        return 'lat: {}, lon: {}'.format(self.lat, self.lon)
