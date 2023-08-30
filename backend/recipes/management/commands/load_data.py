import json

from django.core.management.base import BaseCommand
from recipes.models import Ingredients, Tags


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("--path", type=str, help="file path")

    def handle(self, *args, **options):
        file_path = options["path"]

        with open(file_path, encoding='utf-8') as f:
            jsondata = json.load(f)
            if 'color' in jsondata[0]:
                for line in jsondata:
                    if not Tags.objects.filter(
                       slug=line['slug']).exists():
                        Tags.objects.create(
                            name=line['name'],
                            color=line['color'],
                            slug=line['slug'],
                        )
            elif 'measurement_unit' in jsondata[0]:
                for line in jsondata:
                    if not Ingredients.objects.filter(
                       name=line['name'],
                       measurement_unit=line['measurement_unit']).exists():
                        Ingredients.objects.create(
                            name=line['name'],
                            measurement_unit=line['measurement_unit']
                        )
