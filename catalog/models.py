from django.db import models

NULLABLE = {'blank': True, 'null': True }
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='product/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(to='', on_delete='', verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за покупку')
    created_at = models.DateTimeField(verbose_name='Дата создания') # установка на заполнение при создании
    updated_at = models.DateTimeField(verbose_name='Дата изменения') # установка на заполнение при изменении

    def __str__(self):
        return f'{self.name}, {self.category}, {self.price}, {self.created_at}'


    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('name',)


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)