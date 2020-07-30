#!/usr/bin/python
# -*- coding: utf-8 -*-

# Create your models here.
from django.db import models
# from django.contrib.auth.models import User
from oauth.models import Ouser
from django.urls import reverse
import markdown
from django.utils.html import strip_tags

# 美化中文toc锚点
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension

import re


class Category(models.Model):
    """
    Django 要求模型必须继承 models.Model 类。
    Category 只需要一个简单的分类名 name 就可以了。
    CharField 指定了分类名 name 的数据类型，CharField 是字符型，
    CharField 的 max_length 参数指定其最大长度，超过这个长度的分类名就不能被存入数据库。
    """
    name = models.CharField('文章分类', max_length=100)
    # 新增描述文字
    description = models.TextField('描述', max_length=240, default='izone 是一个使用 Django+Bootstrap4 搭建的个人博客类型网站',
                                   help_text='用来作为SEO中description,长度参考SEO标准',
                                   blank=True)

    def get_absolute_url(self):
        return reverse('blog:category', kwargs={'pk': self.pk})

    def get_post_list(self):
        # 返回当下标签下的文章列表
        return Post.objects.filter(category=self)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        ordering = ['id']


class Tag(models.Model):
    """
    标签 Tag 也比较简单，和 Category 一样。
    再次强调一定要继承 models.Model 类！
    """
    name = models.CharField('标签', max_length=100)
    description = models.TextField('描述', max_length=240, default='izone 是一个使用 Django+Bootstrap4 搭建的个人博客类型网站',
                                   help_text='用来作为SEO中description,长度参考SEO标准',
                                   blank=True)

    def get_absolute_url(self):
        return reverse('blog:tag', kwargs={'pk': self.pk})

    def get_post_list(self):
        # 返回当下标签下的文章列表
        return Post.objects.filter(tags=self)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
        ordering = ['id']


class Post(models.Model):
    """
    文章的数据库表稍微复杂一点，主要是涉及的字段更多。

    verbose_name和第一个参数为字符串，效果相同
    """

    # 默认图片地址
    IMG_LINK = '/static/blog/img/summary.png'

    # 文章标题
    title = models.CharField(max_length=70, verbose_name='文章标题')

    # 文章正文，我们使用了 TextField。
    # 存储比较短的字符串可以使用 CharField，但对于文章的正文来说可能会是一大段文本，因此使用 TextField 来存储大段文本。
    body = models.TextField(verbose_name='文章内容')

    # 新增图片 2:1
    img_link = models.CharField('图片地址', max_length=255, default=IMG_LINK)

    # 这两个列分别表示文章的创建时间和最后一次修改时间，存储时间的字段用 DateTimeField 类型。
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    modified_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    # 文章摘要，可以没有文章摘要，但默认情况下 CharField 要求我们必须存入数据，否则就会报错。
    # 指定 CharField 的 blank=True 参数值后就可以允许空值了。
    # excerpt = models.CharField('文章摘要', max_length=200, default='文章摘要等同于网页description内容，请务必填写...', blank=True)
    excerpt = models.CharField('文章摘要', max_length=300, blank=True)

    # 这是分类与标签，分类与标签的模型我们已经定义在上面。
    # 我们在这里把文章对应的数据库表和分类、标签对应的数据库表关联了起来，但是关联形式稍微有点不同。
    # 我们规定一篇文章只能对应一个分类，但是一个分类下可以有多篇文章，所以我们使用的是 ForeignKey，即一对多的关联关系。
    # 而对于标签来说，一篇文章可以有多个标签，同一个标签下也可能有多篇文章，所以我们使用 ManyToManyField，表明这是多对多的关联关系。
    # 同时我们规定文章可以没有标签，因此为标签 tags 指定了 blank=True。
    # 如果你对 ForeignKey、ManyToManyField 不了解，请看教程中的解释，亦可参考官方文档：
    # https://docs.djangoproject.com/en/1.10/topics/db/models/#relationships
    # on_delete 不写会报错,之后看文档了解
    category = models.ForeignKey(Category, verbose_name='文章分类', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)

    # 文章作者，这里 User 是从 django.contrib.auth.models 导入的。
    # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django 为我们已经写好的用户模型。
    # 这里我们通过 ForeignKey 把文章和 User 关联了起来。
    # 因为我们规定一篇文章只能有一个作者，而一个作者可能会写多篇文章，因此这是一对多的关联关系，和 Category 类似。
    # author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
    author = models.ForeignKey(Ouser, verbose_name='作者', on_delete=models.CASCADE)

    # 新增 views 字段记录阅读量
    views = models.PositiveIntegerField('阅览量', default=0)

    is_carousel = models.BooleanField('轮播', default=False)

    is_top = models.BooleanField('置顶', default=False)

    # 新增点赞数 看看是不是还会报错
    # thumbs_up = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    # reverse 函数，它的第一个参数的值是 'blog:detail'，意思是 blog 应用下的 name=detail 的视图函数，
    # 由于我们在上面通过 app_name = 'blog' 告诉了 Django 这个 URL 模块是属于 blog 应用的，
    # 因此 Django 能够顺利地找到 blog 应用下 name 为 detail 的视图函数，
    # 于是 reverse 函数会去解析这个视图函数对应的 URL，
    # 我们这里 detail 对应的规则就是 post/(?P<pk>[0-9]+)/ 这个正则表达式，
    # 而正则表达式部分会被后面传入的参数 pk 替换，
    # 所以，如果 Post 的 id（或者 pk，这里 pk 和 id 是等价的） 是 255 的话，
    # 那么 get_absolute_url 函数返回的就是 /post/255/ ，这样 Post 自己就生成了自己的 URL。
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    # 阅读量+1,并更新数据库
    # increase_views 方法首先将自身对应的 views 字段的值 +1（此时数据库中的值还没变），
    # 然后调用 save 方法将更改后的值保存到数据库。
    # 注意这里使用了 update_fields 参数来告诉 Django 只更新数据库中 views 字段的值，
    # 以提高效率。
    # 你也许担心如果两个人同时访问一篇文章，
    # 更改数据库中的阅读量字段的值时会不会冲突？
    # 其实不必担心，我们本来就不是精确地统计阅读量，而且个人博客的流量通常也不会很大，
    # 所以偶尔的冲突导致的数据误差是可以忽略不计的。
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def get_pre(self):
        # 小于id，降序排列，第一个，id值最大的
        return Post.objects.filter(id__lt=self.id).order_by('-id').first()

    def get_next(self):
        return Post.objects.filter(id__gt=self.id).order_by('id').first()

    def body_to_markdown(self):
        # 返回markdown转html后的正文
        return markdown.markdown(self.body, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])

    def body_to_markdownandtoc(self):
        # 对文章标题toc处理,以后再做处理
        md = markdown.Markdown(extensions=[
            # 支持 ```
            'markdown.extensions.extra',
            # 代码高亮
            'markdown.extensions.codehilite',
            # toc
            # 记得在顶部引入 TocExtension 和 slugify
            TocExtension(slugify=slugify),
        ])
        # markdown转html后的正文
        self.body = md.convert(self.body)
        # TOC目录
        self.toc = md.toc

    # ordering 属性用来指定文章排序方式，['-created_time'] 指定了依据哪个属性的值进行排序，
    # 这里指定为按照文章发布时间排序，且负号表示逆序排列。列表中可以用多个项，
    # 比如 ordering = ['-created_time', 'title'] ，那么首先依据 created_time 排序，
    # 如果 created_time 相同，则再依据 title 排序。
    # 这样指定以后所有返回的文章列表都会自动按照 Meta 中指定的顺序排序，
    # 因此可以删掉视图函数中对文章列表中返回结果进行排序的代码了。
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    # 复写save函数,自动生成摘要
    # 第二种生成文章摘要的方法
    # 需要显示 post.body 的前 54 的字符，那么可以在模板中使用 {{ post.body | truncatechars:54 }}。
    # 这种方法的一个缺点就是如果前 54 个字符含有块级 HTML 元素标签的话（比如一段代码块），会使摘要比较难看
    # 故我们使用第一种方法
    def save(self, *args, **kwargs):
        # 如果没有填写摘要
        if not self.excerpt:
            # 首先实例化一个 Markdown 类，用于渲染 body 的文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
            # self.excerpt = strip_tags(md.convert(self.body))[:54]
            self.excerpt = strip_tags(md.convert(self.body))[:130]

        # 调用父类的 save 方法将数据保存到数据库中
        super(Post, self).save(*args, **kwargs)


class FriendLink(models.Model):
    name = models.CharField('网站名称', max_length=50)
    description = models.CharField('网站描述', max_length=100, blank=True)
    link = models.URLField('友链地址', help_text='请填写http或https开头的完整形式地址')
    logo = models.URLField('网站LOGO', help_text='请填写http或https开头的完整形式地址', blank=True)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    is_active = models.BooleanField('是否有效', default=True)
    is_show = models.BooleanField('是否首页展示', default=False)

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name
        ordering = ['created_time']

    def __str__(self):
        return self.name

    def get_home_url(self):
        # 提取友链的主页
        u = re.findall(r'(http|https://.*?)/.*?', self.link)
        home_url = u[0] if u else self.link
        return home_url

    def active_to_false(self):
        self.is_active = False
        self.save(update_fields=['is_active'])

    def show_to_false(self):
        self.is_show = True
        self.save(update_fields=['is_show'])


# 时间线功能
class Timeline(models.Model):
    COLOR_CHOICE = (
        ('primary', '基本-蓝色'),
        ('success', '成功-绿色'),
        ('info', '信息-天蓝色'),
        ('warning', '警告-橙色'),
        ('danger', '危险-红色')
    )
    SIDE_CHOICE = (
        ('L', '左边'),
        ('R', '右边'),
    )
    STAR_NUM = (
        (1, '1颗星'),
        (2, '2颗星'),
        (3, '3颗星'),
        (4, '4颗星'),
        (5, '5颗星'),
    )

    side = models.CharField('位置', max_length=1, choices=SIDE_CHOICE, default='L')
    star_num = models.IntegerField('星星个数', choices=STAR_NUM, default=3)
    icon = models.CharField('图标', max_length=50, default='fa fa-pencil')
    icon_color = models.CharField('图标颜色', max_length=20, choices=COLOR_CHOICE, default='info')
    title = models.CharField('标题', max_length=100)
    update_date = models.DateTimeField('更新时间')
    content = models.TextField('主要内容')

    class Meta:
        verbose_name = '时间线'
        verbose_name_plural = verbose_name
        ordering = ['update_date']

    def __str__(self):
        return self.title[:20]

    def content_to_markdown(self):
        return markdown.markdown(self.content,
                                 extensions=['markdown.extensions.extra', ]
                                 )
