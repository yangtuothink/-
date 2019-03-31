"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from django.contrib import admin
from django.views.static import serve

import xadmin
from users.views import IndexView, LoginView, RegisterView, ActiveUserView
from users.views import ForgetPwdView, ResetView, ModifyPwdView, LogoutView
from organization.views import OrgView
from MxOnline.settings import MEDIA_ROOT

# from MxOnline.settings import STATIC_ROOT

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),

    # 验证码
    url(r'^captcha/', include('captcha.urls')),

    # media
    url(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),

    # 主页
    url(r'^$', IndexView.as_view(), name="index"),

    # 登录
    url(r'^login/$', LoginView.as_view(), name="login"),

    # 登出
    url(r'^logout/$', LogoutView.as_view(), name="logout"),

    # 注册
    url(r'^register/$', RegisterView.as_view(), name="register"),

    # 激活
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name="user_active"),

    # 忘记密码
    url(r'^forget/$', ForgetPwdView.as_view(), name="forget_pwd"),

    # 重置密码
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name="reset_pwd"),
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name="modify_pwd"),

    # 课程机构 URL 配置
    url(r'^org/', include('organization.urls', namespace="org")),

    # 课程相关 URL 配置
    url(r'^course/', include('courses.urls', namespace="course")),

    # 用户相关 URL 配置
    url(r'^users/', include('users.urls', namespace="users")),

    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    # 富文本相关url
    # url(r'^ueditor/', include('DjangoUeditor.urls')),

    # 生产环境static url配置
    # url(r'^static/(?P<path>.*)$', serve, {"document_root": STATIC_ROOT}),
]

# 全局404页面配置
handler404 = 'users.views.page_not_found'

# 全局500页面配置
handler500 = 'users.views.page_error'
