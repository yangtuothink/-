# _*_ coding:utf-8 _*_
__author__ = "yangtuo"
__date__ = "2019/3/24 14:20"

from django.conf.urls import url
from .views import UserInfoView

urlpatterns = [
    # 用户信息
    url(r'^info/', UserInfoView.as_view(), name="user_list"),

]
