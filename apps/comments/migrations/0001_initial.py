# Generated by Django 2.2 on 2020-07-15 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_post_is_carousel'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('content', models.TextField(verbose_name='评论内容')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postcomment_related', to=settings.AUTH_USER_MODEL, verbose_name='评论人')),
                ('belong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='blog.Post', verbose_name='所属文章')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='postcomment_child_comments', to='comments.PostComment', verbose_name='父评论')),
                ('rep_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='postcomment_rep_comments', to='comments.PostComment', verbose_name='回复')),
            ],
            options={
                'verbose_name': '文章评论',
                'verbose_name_plural': '文章评论',
                'ordering': ['create_date'],
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='提示时间')),
                ('is_read', models.BooleanField(default=False, verbose_name='是否已读')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='the_comment', to='comments.PostComment', verbose_name='所属评论')),
                ('create_p', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_create', to=settings.AUTH_USER_MODEL, verbose_name='提示创建者')),
                ('get_p', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_get', to=settings.AUTH_USER_MODEL, verbose_name='提示接收者')),
            ],
            options={
                'verbose_name': '提示信息',
                'verbose_name_plural': '提示信息',
                'ordering': ['-create_date'],
            },
        ),
    ]
