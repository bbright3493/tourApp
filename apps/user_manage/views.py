# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from .models import UserProfile, EmailVerifyRecord
from django.db.models import Q
from django.views.generic.base import View
from .froms import LoginForm, RegisterForm, ForgetForm, ModifyPwdForm
from django.contrib.auth.hashers import make_password
from utils.email_send import send_register_email
# Create your views here.

class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})
    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'index.html')
                else:
                    return render(request, 'login.html', {'msg':'用户名未激活'})
            else:
                return render(request, 'login.html', {'msg':'用户名和密码错误'})
        else:
            return render(request, 'login.html',  {'login_form':login_form})


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form':register_form})
    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('email', '')
            t = UserProfile.objects.filter(email=user_name)

            if UserProfile.objects.filter(email=user_name):
                return render(request, 'register.html', {'register_form':register_form,  'msg':'用户已经存在'})
            pass_word = request.POST.get('password', '')
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.is_active = False
            user_profile.password = make_password(pass_word)
            user_profile.save()

            send_register_email(user_name, 'register', )
            return render(request, 'login.html')
        else:
            return render(request, 'register.html', {'register_form':register_form})

class ActiveUserView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email==email)
                user.save()
        else:
            render(request, 'active_fail.html')
        return  render(request, 'login.html')

class ForgetPasswordView(View):
    def get(self, request):
        forget_form = ForgetForm()
        render(request, 'forgetpwd.html', {'forget_form':forget_form})

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get('email', '')
            send_register_email(email, 'forget')
            render(request, 'send_success.html')
        else:
            render(request, 'forgetpwd.html', {'forget_form': forget_form})

class ResetPwdView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                render(request, 'password_reset.html.html', {'email':email})
        else:
            render(request, 'active_fail.html')
        return  render(request, 'login.html')

class ModifyPwd(View):
    def post(self, request):
        reset_form = ModifyPwdForm(request.POST)
        if reset_form.is_valid():
            #判断两个密码是否一样
            #一样则保存密码
            pwd1 = request.POST.get('password1', '')
            pwd2 = request.POST.get('password2', '')
            email = request.POST.get('email', '')
            if pwd1 != pwd2:
                render(request, 'password_reset.html.html', {'email': email, 'msg':'密码不一致'})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd2)
            user.save()
            render(request, 'login.html')
        else:
            email = request.POST.get('email', '')
            render(request, 'password_reset.html.html', {'email':email, 'reset_form':reset_form})
