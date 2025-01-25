import folium
from django.shortcuts import render, get_object_or_404
from pogomap.settings import TIME_ZONE
from pokemon_entities.models import Pokemon, PokemonEntity
from django.utils import timezone
import pytz

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def get_time_now():
    return timezone.localtime(timezone=pytz.timezone(TIME_ZONE))


def show_all_pokemons(request):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemon_entities = PokemonEntity.objects.filter(
        appeared_at__lt=get_time_now(),
        disappeared_at__gt=get_time_now()
    )
    for pokemon in pokemon_entities:
        if pokemon.pokemon.image:
            add_pokemon(
                folium_map, pokemon.lat,
                pokemon.lon,
                request.build_absolute_uri(pokemon.pokemon.image.url)
            )
        else:
            add_pokemon(
                folium_map, pokemon.lat,
                pokemon.lon
            )

    pokemons = Pokemon.objects.all()
    pokemons_on_page = []
    for pokemon in pokemons:
        if pokemon.image:
            pokemons_on_page.append({
                'pokemon_id': pokemon.id,
                'img_url': request.build_absolute_uri(pokemon.image.url),
                'title_ru': pokemon.title_ru,
            })
        else:
            pokemons_on_page.append({
                'pokemon_id': pokemon.id,
                'title_ru': pokemon.title_ru,
            })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemon_entities = PokemonEntity.objects.filter(
        appeared_at__lt=get_time_now(),
        disappeared_at__gt=get_time_now(),
        pokemon=Pokemon.objects.get(id=pokemon_id)
    )
    for pokemon in pokemon_entities:
        if pokemon.pokemon.image:
            add_pokemon(
                folium_map, pokemon.lat,
                pokemon.lon,
                request.build_absolute_uri(pokemon.pokemon.image.url)
            )
        else:
            add_pokemon(
                folium_map, pokemon.lat,
                pokemon.lon
            )

    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    if pokemon.image:
        img_url = request.build_absolute_uri(pokemon.image.url)
    else:
        img_url = DEFAULT_IMAGE_URL

    pokemon_info = {
        "title_ru": pokemon.title_ru,
        "title_en": pokemon.title_en,
        "title_jp": pokemon.title_jp,
        "description": pokemon.description,
        "img_url": img_url,
    }

    if pokemon.previous_evolutions:
        if pokemon.previous_evolutions.image:
            img_url = request.build_absolute_uri(pokemon.previous_evolutions.image.url)
        else:
            img_url = DEFAULT_IMAGE_URL

        pokemon_info["previous_evolution"]= {
            "id": pokemon.previous_evolutions.id,
            "title_ru": pokemon.previous_evolutions.title_ru,
            "img_url": img_url,
        }

    next_pokemon = pokemon.next_evolution.first()
    if next_pokemon:
        if next_pokemon.image:
            img_url = request.build_absolute_uri(next_pokemon.image.url)
        else:
            img_url = DEFAULT_IMAGE_URL

        pokemon_info["next_evolution"]= {
            "id": next_pokemon.id,
            "title_ru": next_pokemon.title_ru,
            "img_url": img_url,
        }


    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon_info
    })
