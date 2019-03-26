from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# 用户表
# 继承了 auth 并拓展了词条
class UserProfile(AbstractUser):
    nickname = models.CharField(max_length=50, verbose_name="昵称", default="")
    birday = models.DateField(verbose_name="生日", null=True)
    gender = models.CharField(max_length=6, choices=(("male", "男"), ("female", "女")), default="female")
    addres = models.CharField(max_length=100, default="")
    mobile = models.CharField(max_length=11, null=True, default="")
    image = models.ImageField(max_length=100, upload_to="image/%Y/%m", default="image/default.png")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name="验证码")
    email = models.EmailField(max_length=50, verbose_name="邮箱")
    send_type = models.CharField(max_length=15,
                                 choices=(("register", "注册"), ("forget", "找回密码"), ("update_email", "修改邮箱")),
                                 verbose_name="验证码类型")
    send_time = models.DateTimeField(default=datetime.now, verbose_name="发送时间")
    """
    datetime.now 这里没有加括号 
        如果加了括号代表的是 class EmailVerifyRecord 被编译的时间被记录
        不加括号代表的是 当class EmailVerifyRecord 进行实例化的时候才会被创建
    """

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{0}({1})".format(self.code, self.email)


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name="标题")
    image = models.ImageField(max_length=200, upload_to="banner/%Y%m", verbose_name="轮播图")
    url = models.URLField(max_length=200, verbose_name="访问地址")
    index = models.IntegerField(default=100, verbose_name="顺序")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name
