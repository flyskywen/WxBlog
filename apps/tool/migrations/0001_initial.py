# Generated by Django 2.2.3 on 2020-08-07 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToolLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='网站名称')),
                ('description', models.CharField(max_length=100, verbose_name='网站描述')),
                ('image_link', models.CharField(default='/static/editor/images/logos/editormd-logo-96x96.png', max_length=30, verbose_name='图标地址')),
                ('link', models.URLField(verbose_name='网站链接')),
                ('order_num', models.IntegerField(default=99, help_text='序号可以用来调整顺序，越小越靠前', verbose_name='序号')),
                ('category', models.CharField(max_length=30, verbose_name='网站分类')),
            ],
            options={
                'verbose_name': '推荐工具',
                'verbose_name_plural': '推荐工具',
                'ordering': ['order_num', 'id'],
            },
        ),
    ]