# -*- coding:utf-8 -*-
__author__ = 'zhoujifeng'
__date__ = '2019/6/25 22:49'

from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
