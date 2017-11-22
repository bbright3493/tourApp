# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

from datetime import datetime

# Create your models here.

class Course(models.Model):
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

    class Mate:
        verbose_name = u'课程'
        verbose_name_plural = verbose_name

