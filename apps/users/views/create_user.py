# -*- coding:utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.utils import IntegrityError
from django.http import HttpResponse
from django.views import View

from users.models import User

__author__ = 'zhoujifeng'
__date__ = '2019/8/29 11:00'
__file_name__ = 'create_user'
__project_name__ = 'ad_django'


class CreateUser(LoginRequiredMixin, View):
    def __init__(self):
        super().__init__()

    def post(self, request):
        username = request.POST['createUsername']
        password = request.POST['password']
        is_active = request.POST['is_active']
        create_result = self.db_create_user(username, password, is_active)
        if create_result == 1:
            return HttpResponse('1')
        elif create_result == -1:
            return HttpResponse('-1')

    # 创建用户 激活/封停
    def db_create_user(self, username, password, is_active):
        if is_active == '0':
            is_active = False
        elif is_active == '1':
            is_active = True

        try:
            User.objects.create_user(username=username, password=password, is_active=is_active)
        except IntegrityError:
            return -1  # 已经创建，无法重复创建
        else:
            return 1  # 创建成功
