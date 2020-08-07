from django.shortcuts import render
from .models import ToolLink
from django.views.generic import ListView


# Create your views here.
# 工具首页
# def toolview(request):
#     return render(request, 'tool/tool.html')


class ToolView(ListView):
    model = ToolLink
    template_name = 'tool/tool.html'
    context_object_name = 'tool_list'
    # ordering = ('order_num', 'id') # model已经排序


# markdown编辑器
def editor_view(request):
    return render(request, 'tool/editor.html')
