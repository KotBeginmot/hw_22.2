from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='наименование')
    overview = models.TextField(verbose_name='описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name, self.overview}'


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    overview = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='product/', verbose_name='превью', **NULLABLE)
    # category = models.CharField(max_length=50, verbose_name='категория')
    category = models.ForeignKey("Category", on_delete=models.CASCADE,
                                 verbose_name='категория')
    purchase_price = models.IntegerField(verbose_name='цеза за покупку')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания', **NULLABLE)
    last_modified_date = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения', **NULLABLE)
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return f'{self.name} - {self.overview}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ContactData(models.Model):
    name = models.CharField(max_length=100, verbose_name='имя')
    phone = models.TextField(verbose_name='телефон')
    text = models.TextField(verbose_name='сообщение')

    def __str__(self):
        return f'Имя: {self.name}, телефон: {self.phone}, сообщение: {self.text}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
