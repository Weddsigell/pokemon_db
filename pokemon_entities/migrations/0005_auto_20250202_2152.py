# Generated by Django 3.1.14 on 2025-02-02 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0004_auto_20250202_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='картинка покемона'),
        ),
    ]
