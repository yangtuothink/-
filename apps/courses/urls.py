# _*_ coding:utf-8 _*_
__author__ = "yangtuo"
__date__ = "2019/3/18 19:32"
from django.conf.urls import url, include
from .views import CourseListView

urlpatterns = [
    # 课程机构列表页
    url(r'^list/$', CourseListView.as_view(), name="course_list"),


]
