# -*- coding:utf-8 -*-
__author__ = 'zhoujifeng'
__date__ = '2019/9/10 16:26'
__file_name__ = 'permissions_middleware'
__project_name__ = 'ad_django'

from django.utils.deprecation import MiddlewareMixin


class PermissionsMiddleware(MiddlewareMixin):
    def process_request(self):
        pass
