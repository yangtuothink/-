# _*_ coding:utf-8 _*_
__author__ = "yangtuo"
__date__ = "2019/3/14 15:08"

import xadmin

from datetime import datetime
from .models import EmailVerifyRecord, Banner, UserProfile
from xadmin import views
from xadmin.plugins.auth import UserAdmin

"""
默认继承的是 auth_user 表, 这里需要我们自己的用户表来关联
这里使用的版本已经自动将 我们扩展的用户表识别到了
因此不需要在补全这个操作了
"""


# class UserProfileAdmin(UserAdmin):
#     def get_form_layout(self):
#     # 此方法是定制 xadmin 用户表的样式来的
#         if self.org_obj:
#             self.form_layout = (
#                 Main(
#                     Fieldset('',  # Fieldset 是横向的显示块
#                              'username', 'password',  # 写多个字段进去就可以按行显示
#                              css_class='unsort no_title'
#                              ),
#                     Fieldset(_('Personal info'),  # 此字段表示 信息块的标题内容, 输入英文是会自动翻译成中文显示
#                              Row('first_name', 'last_name'),  # 使用 Row 就可以实现多字段的同行显示
#                              'email'
#                              ),
#                     Fieldset(_('Permissions'),
#                              'groups', 'user_permissions'
#                              ),
#                     Fieldset(_('Important dates'),
#                              'last_login', 'date_joined'
#                              ),
#                 ),
#                 Side(     # Side 是右侧边栏的显示块
#                     Fieldset(_('Status'),
#                              'is_active', 'is_staff', 'is_superuser',
#                              ),
#                 )
#             )
#         return super(UserAdmin, self).get_form_layout()


# 使能主题功能
class BaseSetting(object):
    enable_themes = True  # 打开主题功能
    use_bootswatch = True  # 打开可选主题库


# 更改后台默认显示信息
class GlobalSetting(object):
    site_title = "羊驼后台管理系统"  # 左上角显示信息
    site_footer = "羊驼总经联合协会"  # 最下面公司信息
    menu_style = "accordion"  # 左侧表名按 APP 折叠


# 邮箱验证码注册
class EmailVerifyRecordAdmin(object):
    list_display = ["code", "email", "send_type", "send_time"]
    search_fields = ["code", "email", "send_type"]
    list_filter = ["code", "email", "send_type", "send_time"]
    model_icon = 'fa fa-envelope-o'  # 自定义 font awesome 图标名


# 轮播图注册
class BannerAdmin(object):
    list_display = ["title", "image", "url", "index", "add_time"]
    search_fields = ["title", "image", "url", "index"]
    list_filter = ["title", "image", "url", "index", "add_time"]


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)

# xadmin.site.register(UserProfile, UserProfileAdmin)
# 如果较老版本不自动识别自己用户表, 在自己手动添加自己扩展用户表后, 使用此命令卸载默认的 xadmin 用户表
# from django.contrib.auth.models import User
# xadmin.site.unregister(User)
