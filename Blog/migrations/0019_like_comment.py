# Generated by Django 4.2.3 on 2023-07-19 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0018_subscriber'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='comment',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Blog.comment'),
        ),
    ]
