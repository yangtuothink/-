# _*_ coding:utf-8 _*_
__author__ = "yangtuo"
__date__ = "2019/3/22 21:37"

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# 判断是否登录
class LoginRequiredMixin(object):

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)
