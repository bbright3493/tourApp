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

from django import  forms
from user_operation.models import UserAsk
import re

class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        regex = '^1[358]\d{9}$|^147\d{8}$|^176\d{8}$'
        p = re.compile(regex)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u'手机号非法', code='mobile_invalid')