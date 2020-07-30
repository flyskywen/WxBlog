from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from .models import PostComment, Notification
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from datetime import datetime
from . import handlers  # 信号

# from .forms import CommentForm;
# Create your views here.

'''
def post_comment(request, post_pk):
    # 先获取被评论的文章，因为后面需要把评论和被评论的文章关联起来。
    # 这里我们使用了 Django 提供的一个快捷函数 get_object_or_404，
    # 这个函数的作用是当获取的文章（Post）存在时，则获取；否则返回 404 页面给用户。
    post = get_object_or_404(Post, pk=post_pk)

    # HTTP 请求有 get 和 post 两种，一般用户通过表单提交数据都是通过 post 请求，
    # 因此只有当用户的请求为 post 时才需要处理表单数据。
    if request.method == 'POST':
        # 用户提交的数据存在 request.POST 中，这是一个类字典对象。
        # 我们利用这些数据构造了 CommentForm 的实例，这样 Django 的表单就生成了。
        form = CommentForm(request.POST)

        # 当调用 form.is_valid() 方法时，Django 自动帮我们检查表单的数据是否符合格式要求。
        if form.is_valid():
            # 检查到数据是合法的，调用表单的 save 方法保存数据到数据库，
            # commit=False 的作用是仅仅利用表单的数据生成 Comment 模型类的实例，但还不保存评论数据到数据库。
            comment = form.save(commit=False)

            # 将评论和被评论的文章关联起来。
            comment.post = post

            # 最终将评论数据保存进数据库，调用模型实例的 save 方法
            comment.save()

            # 重定向到 post 的详情页，实际上当 redirect 函数接收一个模型的实例时，
            # 它会调用这个模型实例的 get_absolute_url 方法，
            # 然后重定向到 get_absolute_url 方法返回的 URL。
            # 回到原本的文章详情页
            return redirect(post)

        else:
            # 检查到数据不合法，重新渲染详情页，并且渲染表单的错误。
            # 因此我们传了三个模板变量给 detail.html，
            # 一个是文章（Post），一个是评论列表，一个是表单 form
            # 注意这里我们用到了 post.comment_set.all() 方法，
            # 这个用法有点类似于 Post.objects.all()
            # 其作用是获取这篇 post 下的的全部评论，
            # 因为 Post 和 Comment 是 ForeignKey 关联的，
            # 因此使用 post.comment_set.all() 反向查询全部评论。
            # 反向查询出post下的所有评论
            comment_list = post.comment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
                       }
            return render(request, 'blog/detail.html', context=context)
    # 不是 post 请求，说明用户没有提交数据，重定向到文章详情页。
    return redirect(post)

'''

user_model = settings.AUTH_USER_MODEL


@login_required
@require_POST
def AddcommentView(request):
    if request.is_ajax() and request.method == "POST":
        data = request.POST
        new_user = request.user

        new_content = data.get('content')
        article_id = data.get('article_id')
        rep_id = data.get('rep_id')

        print(article_id, new_content, rep_id)

        the_article = Post.objects.get(id=article_id)

        if len(new_content) > 1048:
            return JsonResponse({'msg': '你的评论字数超过1048，无法保存。'})

        if not rep_id:
            # 父评论
            new_comment = PostComment(author=new_user, content=new_content, belong=the_article, parent=None,
                                      rep_to=None)
        else:

            # 子评论
            new_rep_to = PostComment.objects.get(id=rep_id)
            new_parent = new_rep_to.parent if new_rep_to.parent else new_rep_to

            new_comment = PostComment(author=new_user, content=new_content, belong=the_article, parent=new_parent,
                                      rep_to=new_rep_to)

        new_comment.save()
        new_point = '#com-' + str(new_comment.id)
        return JsonResponse({'msg': '评论提交成功！', 'new_point': new_point})
    return JsonResponse({'msg': '评论失败！'})


@login_required
def NotificationView(request, is_read=None):
    '''展示提示消息列表'''
    now_date = datetime.now()
    return render(request, 'comment/notification.html', context={'is_read': is_read, 'now_date': now_date})


@login_required
@require_POST
def mark_to_read(request):
    '''将一个消息标记为已读'''
    if request.is_ajax() and request.method == "POST":
        data = request.POST
        user = request.user
        id = data.get('id')
        info = get_object_or_404(Notification, get_p=user, id=id)
        info.mark_to_read()
        return JsonResponse({'msg': 'mark success'})
    return JsonResponse({'msg': 'miss'})


@login_required
@require_POST
def mark_to_delete(request):
    '''将一个消息删除'''
    if request.is_ajax() and request.method == "POST":
        data = request.POST
        user = request.user
        id = data.get('id')
        info = get_object_or_404(Notification, get_p=user, id=id)
        info.delete()
        return JsonResponse({'msg': 'delete success'})
    return JsonResponse({'msg': 'miss'})
