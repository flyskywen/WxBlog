from django.contrib import admin
from .models import ToolLink


# Register your models here.
@admin.register(ToolLink)
class ToolLinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'order_num', 'category')
