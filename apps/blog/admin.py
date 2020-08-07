from django.contrib import admin
from .models import Post, Category, Tag, FriendLink, Timeline


# Register your models here.

# 定制 Post Admin 显示内容
# 定制 Admin 后台
# 在 admin post 列表页面，我们只看到了文章的标题，但是我们希望它显示更加详细的信息，这需要我们来定制 Admin 了，在 admin.py 添加如下代码：
# 添加了创建时间,修改时间,和作者
# class PostAdmin(admin.ModelAdmin):
#     list_display = ['title', 'created_time', 'modified_time', 'author', 'is_carousel', 'is_top', 'views']
#
#
# # 把新增的 PostAdmin 也注册进来
# admin.site.register(Post, PostAdmin)
# admin.site.register(Category)
# admin.site.register(Tag)
# admin.site.register(FriendLink)


# 重写 AdminSite 类的 index() 方法，实现admin下的model排序
# 未实现
class MyAdminSite(admin.AdminSite):

    def index(self, request, extra_context=None):
        if extra_context is None:
            extra_context = {}

        app_list = self.get_app_list(request)
        app_dict = self._build_app_dict(request)

        # dict_keys(['equipment', 'liveos', 'clone', 'oauth2_provider', 'auth'])
        print(app_list, app_dict.keys())

        extra_context['app_list'] = app_list
        return super(MyAdminSite, self).index(request, extra_context)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'description')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'description')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # 这个的作用是给出一个筛选机制，一般按照时间比较好
    date_hierarchy = 'created_time'

    # 除了views
    exclude = ('views',)

    # 在查看修改的时候显示的属性，第一个字段带有<a>标签，所以最好放标题
    list_display = ('id', 'title', 'author', 'created_time', 'modified_time', 'is_top')

    # 设置需要添加<a>标签的字段
    list_display_links = ('title',)

    # 激活过滤器，这个很有用
    list_filter = ('created_time', 'category', 'is_top')

    list_per_page = 50  # 控制每页显示的对象数量，默认是100

    # filter_horizontal = ('tags', 'keywords')  # 给多选增加一个左右添加的框

    # 限制用户权限，只能看到自己编辑的文章
    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)


@admin.register(FriendLink)
class FriendLinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'link', 'created_time', 'is_active', 'is_show')
    date_hierarchy = 'created_time'
    list_filter = ('is_active', 'is_show')


@admin.register(Timeline)
class TimelineAdmin(admin.ModelAdmin):
    list_display = ('title', 'side', 'update_date', 'icon', 'icon_color',)
    fieldsets = (
        ('图标信息', {'fields': (('icon', 'icon_color'),)}),
        ('时间位置', {'fields': (('side', 'update_date', 'star_num'),)}),
        ('主要内容', {'fields': ('title', 'content')}),
    )
    date_hierarchy = 'update_date'
    list_filter = ('star_num', 'update_date')
