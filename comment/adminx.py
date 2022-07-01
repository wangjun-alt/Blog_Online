# from django.contrib import admin
# from .models import Comment
# from blog.custom_site import custom_site
# from blog.base_admin import BaseOwnerAdmin
import xadmin
from .models import Comment


@xadmin.sites.register(Comment)  # 评论管理
class CommentAdmin:
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')

# @admin.register(Comment, site=custom_site)
# class CommentAdmin(BaseOwnerAdmin):
#     list_display = ('target', 'nickname', 'content', 'website', 'created_time')
