# -*- coding:utf-8 -*-
from datetime import datetime

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db import models

__author__ = 'zhoujifeng'
__date__ = '2019/8/29 9:54'
__file_name__ = 'user'
__project_name__ = 'ad_django'


class User(AbstractBaseUser):
    """
    Users within the Django authentication system are represented by this
    model.
媒体
    Username, password and email are required. Other fields are optional.
    """
    GENDER_CHOICES = (
        (u'0', u'男'),
        (u'1', u'女'),
    )
    username = models.CharField(max_length=40, unique=True)
    USERNAME_FIELD = 'username'
    image = models.ImageField(upload_to='media/images/user/', default='media/images/default.png', verbose_name='头像')
    gender = models.PositiveSmallIntegerField(default=0, choices=GENDER_CHOICES, verbose_name='性别')
    email = models.CharField(max_length=64, default='', verbose_name='邮箱')
    is_superuser = models.BooleanField(default=False, verbose_name='是否为管理账号')
    create_time = models.DateTimeField(blank=True, null=True, default=datetime.now, verbose_name="创建时间")
    update_time = models.DateTimeField(blank=True, null=True, default=datetime.now, verbose_name="更新时间")

    objects = UserManager()

    class Meta(AbstractBaseUser.Meta):
        verbose_name = '用户信息'
