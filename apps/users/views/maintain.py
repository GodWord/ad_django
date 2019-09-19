# -*- coding:utf-8 -*-
__author__ = 'zhoujifeng'
__date__ = '2019/9/5 9:57'
__file_name__ = 'maintain'
__project_name__ = 'ad_django'

from django.shortcuts import render
from django.views import View


class Maintain(View):
    def get(self, request):
        return render(request, 'maintain.html')
