# _*_ coding:utf-8 _*_
__author__ = "yangtuo"
__date__ = "2019/3/14 15:59"

from .models import Course, Lesson, Video, CourseResource, BannerCourse
import xadmin


class LessonInline(object):
    model = Lesson
    extar = 0


class VideoInline(object):
    model = Video
    extar = 0


class CourseResourceInline(object):
    model = CourseResource
    extar = 0


# 课程注册
class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_time', 'students',
                    'fav_nums', 'click_nums', 'add_time', 'get_zj_nums', 'go_to']  # 自己定义的函数也可以被当做字段来展示
    search_fields = ['name', 'desc', 'detail', 'degree', 'students', 'fav_nums', 'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_time', 'students', 'fav_nums', 'click_nums',
                   'add_time']
    ordering = ['-click_nums']  # 默认排序 按照点击数倒叙排列
    readonly_fields = ['fav_nums']  # 设置只读, 不可编辑
    list_editable = ['degree', 'desc']  #
    exclude = ['click_nums']  # 设置不可见 readonly_fields 和 exclude 是冲突的, 两个都设置会让 exclude 失效以只读显示
    inlines = [LessonInline, CourseResourceInline]  # 嵌套外键字段的 相关编辑操作, 可以添加多个, 但是不允许嵌套两层

    # refresh_times = [3,5]  # 设置刷新频率

    def queryset(self):  # 实现上下分表, 将轮播课程另外显示
        qs = super(CourseAdmin, self).queryset()
        qs = qs.filter(is_banner=False)
        return qs

    def save_models(self):  # 在保存课程的时候统计课程机构的课程数
        obj = self.new_obj
        obj.save()
        if obj.course_org is not None:
            course_org = obj.course_org
            course_org.course_nums = Course.objects.filter(course_org=course_org).count()
            course_org.save()


# 轮播课程注册
class BannerCourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_time', 'students', 'fav_nums', 'click_nums', 'add_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students', 'fav_nums', 'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_time', 'students', 'fav_nums', 'click_nums', 'add_time']
    ordering = ['-click_nums']
    readonly_fields = ['fav_nums']
    exclude = ['click_nums']
    inlines = [LessonInline, CourseResourceInline]

    def queryset(self):
        qs = super(BannerCourseAdmin, self).queryset()
        qs = qs.filter(is_banner=True)
        return qs


# 章节注册
class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']
    inlines = [VideoInline]


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
xadmin.site.register(BannerCourse, BannerCourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
