# Generated by Django 4.2.4 on 2023-08-18 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='наименование')),
                ('overview', models.TextField(verbose_name='описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='наименование')),
                ('overview', models.TextField(verbose_name='описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='превью')),
                ('purchase_price', models.IntegerField(verbose_name='цеза за покупку')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='дата создания')),
                ('last_modified_date', models.DateTimeField(auto_now=True, null=True, verbose_name='дата последнего изменения')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]