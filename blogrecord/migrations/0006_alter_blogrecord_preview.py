# Generated by Django 4.2.4 on 2023-08-27 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogrecord', '0005_alter_blogrecord_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogrecord',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='blog', verbose_name='превью'),
        ),
    ]
