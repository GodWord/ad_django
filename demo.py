# -*- coding:utf-8 -*-
import os
import pickle

from ad_django.settings import BASE_DIR

__author__ = 'zhoujifeng'
__date__ = '2019/9/3 10:55'
__file_name__ = 'demo'
__project_name__ = 'ad_django'

if __name__ == '__main__':
    with open(os.path.join(BASE_DIR, 'static/pickle/res.pickle'), 'rb') as rb:
        res = pickle.loads(rb.read())
    print(res)
