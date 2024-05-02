import json

from django.conf import settings
from django.core.management.base import BaseCommand

from recipes.models import Ingredients, Tags


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("--path", type=str, help="file path")

    def handle(self, *args, **options):
        tags = f'{settings.BASE_DIR}/recipes/data/tags.json'
        ingredients = f'{settings.BASE_DIR}/recipes/data/ingredients.json'
        with open(tags, encoding='utf-8') as t:
            jsondata = json.load(t)
            for line in jsondata:
                if not Tags.objects.filter(slug=line['slug']).exists():
                    Tags.objects.bulk_create([Tags(
                        name=line['name'],
                        color=line['color'],
                        slug=line['slug'],
                    )])
        with open(ingredients, encoding='utf-8') as i:
            jsondata = json.load(i)
            for line in jsondata:
                if not Ingredients.objects.filter(
                    name=line['name'],
                    measurement_unit=line['measurement_unit']
                ).exists():
                    Ingredients.objects.bulk_create([Ingredients(
                        name=line['name'],
                        measurement_unit=line['measurement_unit']
                    )])
