# _*_ coding:utf-8 _*_
__author__ = "yangtuo"
__date__ = "2019/3/15 19:24"
from django import forms

from django import forms
# from captcha.fields import CaptchaField
from .models import UserProfile


# 登录form
class LoginForm(forms.Form):
    # required=True该字段为必填字段
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)

# # 注册form
# class RegisterForm(forms.Form):
#     email = forms.EmailField(required=True)
#     password = forms.CharField(required=True, min_length=5)
#     # 验证码使用，error_messages修改错误显示信息
#     captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


# # 忘记密码form
# class ForgetForm(forms.Form):
#     email = forms.EmailField(required=True)
#     captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})
#
#
# # 密码修改form
# class ModifyPwdForm(forms.Form):
#     password1 = forms.CharField(required=True, min_length=5)
#     password2 = forms.CharField(required=True, min_length=5)
#
#
# # 修改头像form
# class UploadImageForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['image']
#
#
# # 用户信息form
# class UserInfoForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['nick_name', 'gender', 'birday', 'address', 'mobile']
