# -*- coding:utf-8 -*-
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View

__author__ = 'zhoujifeng'
__date__ = '2019/6/25 22:49'


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
