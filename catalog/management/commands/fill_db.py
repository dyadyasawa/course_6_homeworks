from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        product_list = [
            {'name': 'Генератор безумных идей.',
             'description': 'Отдадим бесплатно, только заберите.',
             'image': '',
             'category': 'Точные приборы.',
             'price': 0,
             'created_at': '',
             'updated_at': ''
             },

            {'name': 'Так себе идейка...',
             'description': 'Зачем платить больше. И так сойдет.',
             'image': '',
             'category': 'Идеи.',
             'price': 30,
             'created_at': '',
             'updated_at': ''
             },

            {'name': 'Хорошая идея.',
             'description': 'Все уже придумано за Вас.',
             'image': '',
             'category': 'Идеи.',
             'price': 80,
             'created_at': '',
             'updated_at': ''
             },

            {'name': 'Отличная идея!',
             'description': 'Идеально! Осталось только реализовать.',
             'image': '',
             'category': 'Идеи.',
             'price': 100,
             'created_at': '',
             'updated_at': ''
             },

            {'name': 'Гениальная идея!!!',
             'description': 'Почувcтвуйте себя творцом!',
             'image': '',
             'category': 'Идеи.',
             'price': 130,
             'created_at': '',
             'updated_at': ''
             },

            {'name': 'Генератор гениальных идей.',
             'description': 'Новейшее изобретение в области генерации идей.',
             'image': '',
             'category': 'Точные приборы.',
             'price': 5000,
             'created_at': '',
             'updated_at': ''
             }
        ]

        category_list = [
            {'name': 'Точные приборы.',
             'description': 'Чудо инженерной техники, впитавшее все современные инновации.'
             },

            {'name': 'Идеи.',
             'description': 'Нечто эфемерное, не поддающееся описанию.'
             }
        ]

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(Category(**category_item))

        Category.objects.bulk_create(category_for_create)

        product_for_create = []
        for product_item in product_list:
            product_for_create.append(Product(**product_item))

        Product.objects.bulk_create(product_for_create)
