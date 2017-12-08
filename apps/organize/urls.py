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

from django.conf.urls import include, url
from .views import UserAskView, OrgView, OrgHomeView,CourseDetailView,OrgDescView,TeacherView, AddFavView, TeacherListView


urlpatterns = [
    url(r'^add_ask/$', UserAskView.as_view(), name='userAsk'),
    url(r'^list/$', OrgView.as_view(), name='org_list'),
    url(r'^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name='org_home'),
    url(r'^course_detail/(?P<org_id>\d+)/$', CourseDetailView.as_view(), name='course'),
    url(r'^org_desc/(?P<org_id>\d+)/$', OrgDescView.as_view(), name='org_desc'),
    url(r'^org_teacher/(?P<org_id>\d+)/$', TeacherView.as_view(), name='teacher'),
    url(r'^add_fav/$', AddFavView.as_view(), name='add_fav'),
    url(r'^teacher_list/$', TeacherListView.as_view(), name='teacher_list'),
]