# _*_ coding:utf-8 _*_
__author__ = "yangtuo"
__date__ = "2019/3/14 15:59"

from .models import Course, Lesson, Video, CourseResource
import xadmin


# 课程注册
class CourseAdmin(object):
    list_display = ["name", "desc", "detail", "degree", "learn_time", "students"]
    search_fields = ["name", "desc", "detail", "degree", "students"]
    list_filter = ["name", "desc", "detail", "degree", "learn_time", "students"]


# 章节注册
class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


# 视频注册
class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['lesson', 'name', 'add_time']


# 课程资源注册
class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course__name', 'name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
