# -*- coding:utf-8 -*-
from datetime import datetime

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager as AbstractBaseUserManager
from django.db import models

__author__ = 'zhoujifeng'
__date__ = '2019/8/29 9:54'
__file_name__ = 'user'
__project_name__ = 'ad_django'


class BaseUserManager(AbstractBaseUserManager):
    def create_user(self, username, password=None, email=None, is_active=True, is_superuser=False):
        """
        Creates and saves a User with the given email and password.
        """
        user = self.model(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, user, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            user,
            password=password,
        )
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, email):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            username,
            password=password,
            email=email,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    GENDER_CHOICES = (
        (u'0', u'男'),
        (u'1', u'女'),
    )
    username = models.CharField(max_length=40, unique=True)
    image = models.ImageField(upload_to='media/images/user/', default='media/images/default.png', verbose_name='头像')
    gender = models.PositiveSmallIntegerField(default=0, choices=GENDER_CHOICES, verbose_name='性别')
    email = models.CharField(max_length=64, null=True, verbose_name='邮箱')
    is_superuser = models.BooleanField(default=False, verbose_name='是否为管理账号')
    create_time = models.DateTimeField(blank=True, null=True, default=datetime.now, verbose_name="创建时间")
    update_time = models.DateTimeField(blank=True, null=True, default=datetime.now, verbose_name="更新时间")

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = BaseUserManager()

    class Meta(AbstractBaseUser.Meta):
        verbose_name = '用户信息'
