# Generated by Django 4.2.4 on 2023-09-07 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('version', '0003_alter_version_versions_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='versions_number',
            field=models.IntegerField(unique=True, verbose_name='номер версии'),
        ),
    ]