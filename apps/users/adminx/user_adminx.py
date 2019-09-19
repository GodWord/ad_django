# -*- coding:utf-8 -*-
__author__ = 'zhoujifeng'
__date__ = '2019/8/29 11:23'
__file_name__ = 'user_adminx'
__project_name__ = 'ad_django'

from django.utils.translation import gettext_lazy as _

import xadmin
from users.forms.my_user_creation_form import MyUserCreationForm, MyUserChangeForm
from users.models import User


class MyUserAdmin(object):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = User
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('email',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    list_display = ['email', 'username', 'is_superuser', 'is_active', 'last_login', 'image']


xadmin.site.register(User, MyUserAdmin)
