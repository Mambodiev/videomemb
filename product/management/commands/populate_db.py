# shop/management/commands/populate_db.py

import random
from datetime import datetime, timedelta

import pytz
from django.core.management.base import BaseCommand

from product.models import Product, Sale


class Command(BaseCommand):
    help = 'Populates the database with random generated data.'

    def add_arguments(self, parser):
        parser.add_argument('--amount', type=int, help='The number of sales that should be created.')

    def handle(self, *args, **options):
        names = ['James', 'John', 'Robert', 'Michael', 'William', 'David', 'Richard', 'Joseph', 'Thomas', 'Charles']
        surname = ['Smith', 'Jones', 'Taylor', 'Brown', 'Williams', 'Wilson', 'Johnson', 'Davies', 'Patel', 'Wright']
        products = [
            Product.objects.get_or_create(name='Socks', aliexpress_price=6.5), Product.objects.get_or_create(name='Pants', aliexpress_price=12),
            Product.objects.get_or_create(name='T-Shirt', aliexpress_price=8), Product.objects.get_or_create(name='Boots', aliexpress_price=9),
            Product.objects.get_or_create(name='Sweater', aliexpress_price=3), Product.objects.get_or_create(name='Underwear', aliexpress_price=9),
            Product.objects.get_or_create(name='Leggings', aliexpress_price=7), Product.objects.get_or_create(name='Cap', aliexpress_price=5),
        ]
        amount = options['amount'] if options['amount'] else 2500
        for i in range(0, amount):
            dt = pytz.utc.localize(datetime.now() - timedelta(days=random.randint(0, 1825)))
            sale = Sale.objects.create(
                customer_full_name=random.choice(names) + ' ' + random.choice(surname),
                product=random.choice(products)[0],
                payment_method=random.choice(Sale.PAYMENT_METHODS)[0],
                successful=True if random.randint(1, 2) == 1 else False,
            )
            sale.time = dt
            sale.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database.'))
