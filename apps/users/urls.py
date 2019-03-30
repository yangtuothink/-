# _*_ coding:utf-8 _*_
__author__ = "yangtuo"
__date__ = "2019/3/24 14:20"

from django.conf.urls import url
from .views import UserInfoView, UploadImageView, UpdatePwdView, MyFavTeacherView
from .views import SendEmailCodeView, UpdateEmailView, MyCourseView, MyFavOrgView
from .views import MyFavCoureseView, MyMessageView

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

    # 用户中心我的课程
    url(r'^mycourse/', MyCourseView.as_view(), name="mycourse"),

    # 用户中心收藏课程机构
    url(r'^myfav/org/', MyFavOrgView.as_view(), name="myfav_org"),

    # 用户中心收藏授课讲师
    url(r'^myfav/teacher/', MyFavTeacherView.as_view(), name="myfav_teacher"),

    # 用户中心收藏课程
    url(r'^myfav/course/', MyFavCoureseView.as_view(), name="myfav_course"),

    # 用户中心我的消息
    url(r'^mymessage/', MyMessageView.as_view(), name="mymessage"),

]
