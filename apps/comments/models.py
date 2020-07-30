from django.db import models
from blog.models import Post
from oauth.models import Ouser
import markdown


# Create your models here.
class Comment(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(class)s_related',
    #                            verbose_name='评论人', on_delete=models.CASCADE)
    author = models.ForeignKey(Ouser, related_name='%(class)s_related',
                               verbose_name='评论人', on_delete=models.CASCADE)

    create_date = models.DateTimeField('创建时间', auto_now_add=True)
    content = models.TextField('评论内容')
    parent = models.ForeignKey('self', verbose_name='父评论', related_name='%(class)s_child_comments', blank=True,
                               null=True, on_delete=models.CASCADE)
    rep_to = models.ForeignKey('self', verbose_name='回复', related_name='%(class)s_rep_comments',
                               blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        # 这是一个元类，用来继承的
        abstract = True

    def __str__(self):
        return self.content[:20]

    def content_to_markdown(self):
        to_md = markdown.markdown(self.content,
                                  safe_mode='escape',
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                  ])
        # 表情
        # return get_emoji_imgs(to_md)
        return to_md


class PostComment(Comment):
    belong = models.ForeignKey(Post, related_name='post_comments', verbose_name='所属文章',
                               on_delete=models.CASCADE)

    class Meta:
        verbose_name = '文章评论'
        verbose_name_plural = verbose_name
        ordering = ['create_date']


class Notification(models.Model):
    # create_p = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='提示创建者', related_name='notification_create',
    #                              on_delete=models.CASCADE)
    create_p = models.ForeignKey(Ouser, verbose_name='提示创建者', related_name='notification_create',
                                 on_delete=models.CASCADE)
    # get_p = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='提示接收者', related_name='notification_get',
    #                           on_delete=models.CASCADE)
    get_p = models.ForeignKey(Ouser, verbose_name='提示接收者', related_name='notification_get',
                              on_delete=models.CASCADE)
    comment = models.ForeignKey(PostComment, verbose_name='所属评论', related_name='the_comment',
                                on_delete=models.CASCADE)
    create_date = models.DateTimeField('提示时间', auto_now_add=True)
    is_read = models.BooleanField('是否已读', default=False)

    def mark_to_read(self):
        # 修改为已读
        self.is_read = True
        self.save(update_fields=['is_read'])

    class Meta:
        verbose_name = '提示信息'
        verbose_name_plural = verbose_name
        ordering = ['-create_date']

    def __str__(self):
        # return '{}@了{}'.format(self.create_p, self.get_p)
        return f'{self.create_p}@了{self.get_p}'
