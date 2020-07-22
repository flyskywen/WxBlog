from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


# Create your models here.
'''
。对于 Django 内置的 User 模型， 仅包含以下一些主要的属性：

username，即用户名
password，密码
email，邮箱
first_name，名
last_name，姓

对于一些网站来说，用户可能还包含有昵称、头像、个性签名等等其它属性，因此仅仅使用 Django 内置的 User 模型是不够。
好在 Django 用户系统遵循可拓展的设计原则，我们可以方便地拓展 User 模型。
'''


class Ouser(AbstractUser):
    link = models.URLField('个人网址', blank=True, help_text='提示：网址必须填写以http开头的完整形式')
    avatar = ProcessedImageField(upload_to='avatar/%Y/%m/%d',
                                 default='avatar/default.png',
                                 verbose_name='头像',
                                 processors=[ResizeToFill(80, 80)]
                                 )

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.username
