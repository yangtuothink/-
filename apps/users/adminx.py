# _*_ coding:utf-8 _*_
__author__ = "yangtuo"
__date__ = "2019/3/14 15:08"

import xadmin
from .models import EmailVerifyRecord, Banner
from xadmin import views


# 使能主题功能
class BaseSetting(object):
    enable_themes = True  # 打开主题功能
    use_bootswatch = True  # 打开可选主题库


# 更改后台默认显示信息
class GlobalSetting(object):
    site_title = "羊驼后台管理系统"     # 左上角显示信息
    site_footer = "羊驼总经联合协会"    # 最下面公司信息
    menu_style = "accordion"    # 左侧表名按 APP 折叠


# 邮箱验证码注册
class EmailVerifyRecordAdmin(object):
    list_display = ["code", "email", "send_type", "send_time"]
    search_fields = ["code", "email", "send_type"]
    list_filter = ["code", "email", "send_type", "send_time"]


# 轮播图注册
class BannerAdmin(object):
    list_display = ["title", "image", "url", "index", "add_time"]
    search_fields = ["title", "image", "url", "index"]
    list_filter = ["title", "image", "url", "index", "add_time"]


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
