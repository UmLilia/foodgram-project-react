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
            tag_list = []
            for line in jsondata:
                tag_list.append(Tags(**line))
            Tags.objects.bulk_create(tag_list)
        with open(ingredients, encoding='utf-8') as i:
            jsondata = json.load(i)
            ingredients_list = []
            for line in jsondata:
                ingredients_list.append(Ingredients(**line))
            Ingredients.objects.bulk_create(ingredients_list)
