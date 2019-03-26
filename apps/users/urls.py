# _*_ coding:utf-8 _*_
__author__ = "yangtuo"
__date__ = "2019/3/24 14:20"

from django.conf.urls import url
from .views import UserInfoView, UploadImageView, UpdatePwdView
from .views import SendEmailCodeView, UpdateEmailView

urlpatterns = [
    # 用户个人中心信息
    url(r'^info/', UserInfoView.as_view(), name="user_info"),

    # 用户个人中心头像上传
    url(r'^image/upload', UploadImageView.as_view(), name="image_upload"),

    # 用户个人中心修改密码
    url(r'^update/pwd', UpdatePwdView.as_view(), name="update_pwd"),

    # 用户中心发送验证码
    url(r'^sendemail_code/', SendEmailCodeView.as_view(), name="sendemail_code"),

    # 用户中心修改邮箱
    url(r'^update_email/', UpdateEmailView.as_view(), name="update_email"),

]
