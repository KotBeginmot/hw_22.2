from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class BlogRecord(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug')
    content = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='blog', verbose_name='превью', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    feature = models.BooleanField(verbose_name='признак публикации')
    views_count = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'запись блога'
        verbose_name_plural = 'записи блогов'
