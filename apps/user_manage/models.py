# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


class UserProfile(AbstractUser):
    nike_name = models.CharField(max_length=50, verbose_name=u'昵称', default='')
    birthday = models.DateField(verbose_name='生日', null=True, blank=True)
    gender = models.CharField(max_length=10, choices=(('male', u'男'),('female', u'女')), default='')
    address = models.CharField(max_length=100, default=u'')
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to='image/%Y/%X', default='image/default')

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.user_name


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u'验证码')
    email = models.EmailField(max_length=50, verbose_name=u'邮箱')
    send_type = models.CharField(choices=(('register', u'注册'), ('forget', u'忘记密码')), max_length=10, verbose_name=u'验证类型')
    send_time = models.DateTimeField(default=datetime.now,  verbose_name=u'验证时间')

    class Meta:
        verbose_name = u'邮箱验证码'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}{1}'.format(self.code, self.email)

class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'标题')
    image = models.ImageField(upload_to='banner/%Y/%m', verbose_name=u'轮播图')
    url = models.URLField(max_length=200, verbose_name=u'访问地址')
    index = models.IntegerField(default=100, verbose_name=u'顺序')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'轮播图'
        verbose_name_plural = verbose_name
