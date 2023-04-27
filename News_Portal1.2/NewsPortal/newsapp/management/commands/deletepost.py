from django.core.management.base import BaseCommand, CommandError
from newsapp.models import Post, Category


class Command(BaseCommand):
    help = 'Deleting publications'  # Показывает подсказку при вводе "python manage.py <ваша команда> --help"
    missing_args_message = 'Not enough arguments'
    # requires_migrations_checks = True  # напоминать ли о миграциях. Если тру — то будет напоминание о том, что не
    # # сделаны все миграции (если такие есть)

    def add_arguments(self, parser):
        parser.add_argument('category', type=str)

    def handle(self, *args, **options):
        self.stdout.readable()
        self.stdout.write('Confirm deletion: y/n')  # Запрашиваем у пользователя подтверждение удаления
        answer = input()  # Считываем подтверждение
        if answer == 'y':  # В случае подтверждения удаляем
            category = Category.objects.get(name=options['category'])
            Post.objects.filter(postCategory=category).delete()
            self.stdout.write(self.style.SUCCESS('Deletion performed!'))
            return

        self.stdout.write(self.style.ERROR('Deletion failed!'))  # В случае неправильного подтверждения, говорим что
        # в доступе отказано

# class Command(BaseCommand):
#     help = 'Подсказка вашей команды'
#
#     def add_arguments(self, parser):
#         parser.add_argument('category', type=str)
#
#     def handle(self, *args, **options):
#         answer = input(f'Вы правда хотите удалить все статьи в категории {options["category"]}? yes/no ')
#
#         if answer != 'yes':
#             self.stdout.write(self.style.ERROR('Отменено'))
#
#         try:
#             category = Category.objects.get(name=options['category'])
#             Post.objects.filter(category == category).delete()
#             self.stdout.write(self.style.SUCCESS(
#                 f'Succesfully deleted all news from category {category.name}'))  # в случае неправильного подтверждения говорим, что в доступе отказано
#         except Post.DoesNotExist:
#             self.stdout.write(self.style.ERROR(f'Could not find category {category.name}'))