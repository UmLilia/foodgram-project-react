import logging
import json

from django.conf import settings
from django.core.management.base import BaseCommand

from recipes.models import Ingredients, Tags


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("--path", type=str, help="file path")

    def handle(self, *args, **options):
        file_path = settings.BASE_DIR

        with open(
            f'{file_path}/recipes/data/ingredients.json',
            encoding='utf-8'
        ) as f:
            jsondata = json.load(f)
            tags_data = [
                {'name': 'Завтрак', 'color': '#E26C2D', 'slug': 'breakfast'},
                {'name': 'Обед', 'color': '#49B64E', 'slug': 'lunch'},
                {'name': 'Ужин', 'color': '#8775D2', 'slug': 'dinner'}
            ]
            try:
                Tags.objects.bulk_create(Tags(**tag) for tag in tags_data)
            except Exception as error:
                logging.error({error})
            if 'measurement_unit' in jsondata[0]:
                for line in jsondata:
                    if not Ingredients.objects.filter(
                       name=line['name'],
                       measurement_unit=line['measurement_unit']).exists():
                        Ingredients.objects.bulk_create([Ingredients(
                            name=line['name'],
                            measurement_unit=line['measurement_unit']
                        )])
