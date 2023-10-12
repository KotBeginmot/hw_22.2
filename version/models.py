from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Version(models.Model):
    product = models.ForeignKey('catalog.Product', on_delete=models.CASCADE, verbose_name='продукт')
    versions_number = models.IntegerField(verbose_name='номер версии')
    versions_name = models.CharField(max_length=150, verbose_name="имя версии")
    versions_activity = models.BooleanField(default=False, verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.product},{self.versions_number},{self.versions_name},{self.versions_activity}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
