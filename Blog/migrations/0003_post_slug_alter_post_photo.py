# Generated by Django 4.2.3 on 2023-07-14 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_post_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='', unique=True, verbose_name='Читаемый URL'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to='media/%Y', verbose_name='Изображение'),
        ),
    ]