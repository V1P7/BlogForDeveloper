# Generated by Django 4.2.3 on 2023-07-16 20:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Blog', '0010_alter_dislike_post_alter_dislike_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='disliked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='like',
            name='liked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Кто поставил оценку'),
        ),
    ]
