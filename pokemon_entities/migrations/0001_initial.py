# Generated by Django 3.1.14 on 2025-01-19 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ru', models.CharField(max_length=100, verbose_name='имя на русском')),
                ('title_en', models.CharField(max_length=100, verbose_name='имя на английском')),
                ('title_jp', models.CharField(max_length=100, verbose_name='имя на японском')),
                ('description', models.TextField(verbose_name='описание покемона')),
                ('image', models.ImageField(blank=True, null=True, upload_to=models.CharField(max_length=100, verbose_name='имя на английском'), verbose_name='картинка покемона')),
                ('previous_evolutions', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_evolution', to='pokemon_entities.pokemon', verbose_name='следующая эволюция')),
            ],
        ),
        migrations.CreateModel(
            name='PokemonEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField(verbose_name='Широта')),
                ('lon', models.FloatField(verbose_name='Долгота')),
                ('appeared_at', models.DateTimeField(null=True, verbose_name='когда появляется')),
                ('disappeared_at', models.DateTimeField(null=True, verbose_name='когда пропадает')),
                ('level', models.IntegerField(blank=True, null=True, verbose_name='уровень')),
                ('health', models.IntegerField(blank=True, null=True, verbose_name='здоровье')),
                ('strength', models.IntegerField(blank=True, null=True, verbose_name='сила')),
                ('defence', models.IntegerField(blank=True, null=True, verbose_name='защита')),
                ('stamina', models.IntegerField(blank=True, null=True, verbose_name='выносливость')),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.pokemon', verbose_name='Тип покемона')),
            ],
        ),
    ]
