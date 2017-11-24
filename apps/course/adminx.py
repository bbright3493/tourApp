# -*- coding: utf-8 -*-

import xadmin

from .models import *


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_time', 'students', 'fav_num', 'image', 'click_num','add_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_time', 'students', 'fav_num', 'image', 'click_num']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_time', 'students', 'fav_num', 'image', 'click_num','add_time']

class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course', 'name', 'add_time']

class VidepAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']

class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download', 'add_time']

xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
xadmin.site.register(Video, VidepAdmin)
