#! usr/bin/python
#coding=utf-8

'''
模块名称：
模块主要功能：
模块实现的方法：
模块对外接口：
模块作者：
编写时间：
修改说明：
修改时间：
'''

from django.conf.urls import patterns, include, url
from .views import UserAskView, OrgView


urlpatterns = [
    url(r'^add_ask/$', UserAskView.as_view(), name='userAsk'),
    url(r'^list/$', OrgView.as_view(), name='org_list'),
]