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

from random import Random
from user_manage.models import EmailVerifyRecord
from django.core.mail import send_mail
from tourApp.settings import EMAIL_FROM


def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlNmMnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str

def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    emai_title = ''
    email_body = ''
    if send_type == 'register':
        emai_title = '注册激活链接'
        email_body = '点击下面链接激活你的账号：http://127.0.0.1:8000/active/{0}'.format(code)
        send_status = send_mail(emai_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == 'forget':
        emai_title = '注册密码重置'
        email_body = '点击下面链接重置你的密码：http://127.0.0.1:8000/reset/{0}'.format(code)
        send_status = send_mail(emai_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass


