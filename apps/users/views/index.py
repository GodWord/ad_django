# -*- coding:utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

__author__ = 'zhoujifeng'
__date__ = '2019/9/4 16:09'
__file_name__ = 'index'
__project_name__ = 'ad_django'


class Index(LoginRequiredMixin, View):

    def get(self, request):
        print(request.user.is_superuser)
        return render(request, "index.html")
