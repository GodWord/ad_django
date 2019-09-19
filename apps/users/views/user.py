# -*- coding:utf-8 -*-

__author__ = 'zhoujifeng'
__date__ = '2019/9/4 17:06'
__file_name__ = 'user'
__project_name__ = 'ad_django'

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View


class User(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, "user.html")

    def post(self):
        pass
