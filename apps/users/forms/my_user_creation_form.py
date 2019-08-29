# -*- coding:utf-8 -*-
__author__ = 'zhoujifeng'
__date__ = '2019/8/29 11:20'
__file_name__ = 'my_user_creation_form'
__project_name__ = 'ad_django'

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import User


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='邮箱地址')
    password1 = forms.CharField(label='密码', widget=forms.PasswordInput)
    password2 = forms.CharField(label='确认密码', widget=forms.PasswordInput)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("密码两次输入不一致")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = User

        fields = ('username', 'email')
