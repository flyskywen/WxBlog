# Generated by Django 2.2 on 2020-07-14 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200713_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_carousel',
            field=models.BooleanField(default=False, verbose_name='轮播'),
        ),
    ]
