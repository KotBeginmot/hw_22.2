import os
import random
from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.create(name='Овощи', overview='Полезные , не вкусные')
        Category.objects.create(name='Фрукты', overview='Полезные , вкусные')
        PATH = 'data.json'
        product = ['яблоки', 'картофель', 'бананы', 'капуста', 'помидоры', 'огурцы', 'арбузы', ]
        product_id = [1, 2, 1, 2, 2, 2, 1]
        product_overview = ['Вкусные ,сочные ', 'полезный', 'Вкусные', 'полезная ,сочная',
                            'Вкусные ,сочные ', 'Вкусные ,сочные ', 'Вкусные , очень сочные ']

        os.system(f'python3 manage.py dumpdata catalog.Category > {PATH}')
        Product.objects.all().delete()
        os.system(f'python3 manage.py loaddata {PATH}')

        for_create = []
        for t1, t2, t3 in zip(product, product_id, product_overview):
            for_create.append(Product(**{
                'name': t1,
                'overview': t3,
                'category_id': t2,
                'purchase_price': random.randint(50, 150)
            }))
        Product.objects.bulk_create(for_create)
