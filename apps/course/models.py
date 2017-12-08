# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

from datetime import datetime
from organize.models import CourseOrg, Teacher

# Create your models here.

class Course(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name=u'课程机构', null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name=u'课程名')
    desc = models.CharField(max_length=300, verbose_name=u'课程描述')
    detail = models.TextField(verbose_name=u'课程详情')
    degree = models.CharField(max_length=5, choices=(('cj', '初级'),('zj','中级'),('gj','高级')), verbose_name=u'课程等级')
    learn_time = models.IntegerField(default=0, verbose_name=u'学习时长')
    students = models.IntegerField(default=0, verbose_name=u'学习人数')
    fav_num = models.IntegerField(default=0, verbose_name=u'收藏人数')
    image = models.ImageField(upload_to='courses/%Y/%m', verbose_name=u'课程封面')
    click_num = models.IntegerField(default=0, verbose_name=u'点击数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'加入时间')
    category = models.CharField(default=u'后端开发', max_length=100, verbose_name=u'课程类型')
    tag = models.CharField(default=u'', max_length=50, verbose_name=u'课程标签')
    teacher = models.ForeignKey(Teacher, verbose_name=u'授课教师', null=True, blank=True)
    youneed_know = models.CharField(default=u'', max_length=200, verbose_name=u'课程须知')
    teacher_tell = models.CharField(default=u'', max_length=200, verbose_name=u'教师告知')

    class Meta:
        verbose_name = u'课程列表'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def get_lesson_num(self):
        return self.lesson_set.all().count()

    def get_student(self):
        return self.usercourse_set.all()[:5]

    def get_course_lesson(self):
        return self.lesson_set.all()

class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u'课程')
    name = models.CharField(max_length=100, verbose_name=u'章节名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'章节'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def get_lesson_video(self):
        return self.video_set.all()

class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u'章节')
    name = models.CharField(max_length=100, verbose_name=u'视频名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')
    url = models.CharField(max_length=100, verbose_name=u'访问地址', default=u'')
    learn_time = models.IntegerField(default=0, verbose_name=u'学习时长')
    class Meta:
        verbose_name = u'视频'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u'课程')
    name = models.CharField(max_length=100, verbose_name=u'名称')
    download = models.FileField(upload_to='course/resource/%Y/%m', verbose_name=u'下载地址')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程资源'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

