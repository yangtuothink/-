from datetime import datetime
from django.db import models
from organization.models import CourseOrg


# Create your models here.

# 课程表
class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg, verbose_name="课程机构", null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name="课程名称")
    desc = models.CharField(max_length=300, verbose_name="课程描述")
    detail = models.TextField(verbose_name="课程详情")
    """
    TextField 可以对内容无限制的输入, 避免了使用 CharField 的 max_length 上限问题
    在这里临时使用 TextField 后续使用富文本编辑器的时候会另做更改
    """
    degree = models.CharField(max_length=2, choices=(("cj", "初级"), ("zj", "中级"), ("gj", "高级")), verbose_name="难度")
    learn_time = models.IntegerField(default=0, verbose_name="学习时长(分钟数)")
    students = models.IntegerField(default=0, verbose_name="学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏")
    image = models.ImageField(max_length=100, upload_to="courses/%Y%m", verbose_name="封面图")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 章节表
class Lesson(models.Model):
    # 数据库中的一对多和多对一都可以用Django的外键完成
    course = models.ForeignKey(Course, verbose_name="课程")
    name = models.CharField(max_length=100, verbose_name="章节名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name


# 视频表
class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name="章节")
    name = models.CharField(max_length=100, verbose_name="视频名")
    url = models.CharField(max_length=200, verbose_name="访问地址", default="")
    learn_time = models.IntegerField(default=0, verbose_name="学习时长(分钟数)")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name


# 课程资源表
class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name="课程")
    name = models.CharField(max_length=100, verbose_name="视频名")
    # 后台中可以生成上传文件的按钮
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name=u"资源文件", max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name
