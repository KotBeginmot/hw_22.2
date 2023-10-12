# Generated by Django 4.2.4 on 2023-09-05 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0005_alter_contactdata_options_alter_contactdata_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('versions_number', models.ImageField(upload_to='', verbose_name='номер версии')),
                ('versions_name', models.CharField(max_length=150, verbose_name='имя версии')),
                ('versions_activity', models.BooleanField(default=False, verbose_name='признак текущей версии')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='продукт')),
            ],
            options={
                'verbose_name': 'Версия',
                'verbose_name_plural': 'Версии',
            },
        ),
    ]
