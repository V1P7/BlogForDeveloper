# Generated by Django 4.2.3 on 2023-07-16 20:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Blog', '0013_alter_dislike_disliked_alter_like_liked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dislike',
            name='disliked',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='dislike',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.post'),
        ),
        migrations.AlterField(
            model_name='dislike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='like',
            name='liked',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='like',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.post'),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
