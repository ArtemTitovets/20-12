# Generated by Django 4.2.7 on 2023-12-10 18:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0002_alter_post_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='subscribes',
            field=models.ManyToManyField(related_name='categories', to=settings.AUTH_USER_MODEL, verbose_name='Подписчики'),
        ),
    ]
