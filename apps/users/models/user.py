# -*- coding:utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models

__author__ = 'zhoujifeng'
__date__ = '2019/8/29 9:54'
__file_name__ = 'user'
__project_name__ = 'ad_django'


class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.
媒体
    Username, password and email are required. Other fields are optional.
    """
    nickname = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='media/images/user/', default='media/images/default.png', verbose_name='头像')

    class Meta(AbstractUser.Meta):
        verbose_name = '用户信息'

