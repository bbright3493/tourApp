# -*- coding: utf-8 -*-

"""tourApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from xadmin.plugins import xversion
import xadmin
from user_manage.views import LoginView, RegisterView, ActiveUserView, ForgetPasswordView, ResetPwdView, ModifyPwd
from django.views.generic import TemplateView
from organize.views import OrgView
from tourApp.settings import MEDIA_ROOT
from django.views.static import serve

#version模块自动注册需要版本控制的 Model
xversion.register_models()

xadmin.autodiscover()

urlpatterns = [
    url(r'xadmin/', include(xadmin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url('^login/$', LoginView.as_view(), name='login'),
    url('^register/$', RegisterView.as_view(), name='register'),
    url('^captcha/', include('captcha.urls')),
    url(r'^active/(?P<activate_code>.*)/$', ActiveUserView.as_view(), name='user_active'),
    url(r'^forget/$', ForgetPasswordView.as_view(), name='forget_pwd'),
    url(r'^reset/(?P<activate_code>.*)/$', ResetPwdView.as_view(), name='reset_pwd'),
    url(r'^modify/$', ModifyPwd.as_view(), name='modify_pwd'),
    url(r'^org_list/$', OrgView.as_view(), name='org_list'),

    url(r'^media/(?P<path>.*)$', serve, {'document_root':MEDIA_ROOT}),
    url(r'^org/$', include('organize.urls'), name='org_list'),
]