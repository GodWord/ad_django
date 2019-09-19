# -*- coding:utf-8 -*-
__author__ = 'zhoujifeng'
__date__ = '2019/8/29 9:54'
__file_name__ = 'user'
__project_name__ = 'ad_django'

from datetime import datetime

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager as AbstractBaseUserManager
from django.contrib.auth.models import _user_has_perm
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseUserManager(AbstractBaseUserManager):
    def create_user(self, username, password=None, email=None, is_active=True, is_staff=False, is_superuser=False):
        """
        Creates and saves a User with the given email and password.
        """
        user = self.model(
            username=username,
            email=email,
            is_staff=is_staff,
            is_active=is_active,
            is_superuser=is_superuser
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
        user.is_staff = True

        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    GENDER_CHOICES = (
        (u'0', u'男'),
        (u'1', u'女'),
    )

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('必填. 150 字符以内。 只能输入:字母、数字和 @.+-_ '),
        validators=[username_validator],
        error_messages={
            'unique': _("具有该用户名的用户已存在。"),
        },
    )
    image = models.ImageField(upload_to='media/images/user/', default='media/images/default.png', verbose_name='头像')
    gender = models.PositiveSmallIntegerField(default=0, choices=GENDER_CHOICES, verbose_name='性别')
    email = models.CharField(max_length=64, null=True, verbose_name='邮箱')
    is_superuser = models.BooleanField(default=False, verbose_name='是否为管理账号')

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('指定用户是否可以登录此管理站点。'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ))
    create_time = models.DateTimeField(blank=True, null=True, default=datetime.now, verbose_name="创建时间")
    update_time = models.DateTimeField(blank=True, null=True, default=datetime.now, verbose_name="更新时间")

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = BaseUserManager()

    class Meta(AbstractBaseUser.Meta):
        verbose_name = '用户信息'

    def has_perm(self, perm, obj=None):
        return _user_has_perm(self, perm, obj=obj)

    def has_perms(self, perm_list, obj=None):
        for perm in perm_list:
            if not self.has_perm(perm, obj):
                return False
        return True
