# _*_ coding:utf-8 _*_
__author__ = "yangtuo"
__date__ = "2019/3/18 19:32"
from django.conf.urls import url, include
from .views import OrgView, AddUserAskView

urlpatterns = [
    # 课程机构列表页
    url(r'^list/$', OrgView.as_view(), name="org_list"),
    url(r'^add_ask/$', AddUserAskView.as_view(), name="add_ask"),
    url(r'^home/(?P<org_id>\d+)/$', AddUserAskView.as_view(), name="add_ask")

]
