# Generated by Django 4.2.7 on 2023-12-13 17:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0003_category_subscribes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='subscribes',
        ),
        migrations.AddField(
            model_name='category',
            name='subscribers',
            field=models.ManyToManyField(blank=True, related_name='categories', to=settings.AUTH_USER_MODEL, verbose_name='Подписчики'),
        ),
    ]
