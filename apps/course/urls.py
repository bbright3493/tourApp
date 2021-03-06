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
from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^list/$', CourseListView.as_view(), name='course_list'),
    url(r'^course_detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name='detail'),
    url(r'^course_video/(?P<course_id>\d+)/$', CourseVideoView.as_view(), name='video'),
    url(r'^course_Comments/(?P<course_id>\d+)/$', CourseCommentsView.as_view(), name='comments'),
    url(r'^add_comment/$', AddComment.as_view(), name='add_comment'),
    ]