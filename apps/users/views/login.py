# -*- coding:utf-8 -*-
__author__ = 'zhoujifeng'
__date__ = '2019/6/24 21:10'

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic.base import View


class LoginView(View):
    # login_url = '/login/'
    # redirect_field_name = 'index'

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)  # 使用 Django 的 authenticate 方法来验证
        if user:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {
                'login_err': 'Please recheck your username or password !'
            })
