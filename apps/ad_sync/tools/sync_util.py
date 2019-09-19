# -*- coding:utf-8 -*-
from ad_django.settings import LDAP_URI, SERVER_USER, SERVER_PASSWORD, BASE_DN

__author__ = 'zhoujifeng'
__date__ = '2019/5/29 11:49'

import json
import logging

from ldap3 import Server, Connection, NTLM, ALL, ALL_ATTRIBUTES

logger = logging.getLogger('ad')

server1 = Server(LDAP_URI, get_info=ALL, connect_timeout=5)
LDAP_SERVER_POOL = [server1]


class SyncUtil(object):
    """
    AD用户操作
    """

    def __init__(self):
        """
        初始化
        """
        self.conn = Connection(  # 配置服务器连接参数
            server=LDAP_SERVER_POOL,
            auto_bind=True,
            authentication=NTLM,  # 连接Windows AD需要配置此项
            read_only=False,  # 禁止修改数据：True
            user=SERVER_USER,  # 管理员账户
            password=SERVER_PASSWORD,
        )

        self.active_base_dn = BASE_DN  # 正式员工账户所在OU
        self.search_filter = '(objectclass=person)'  # 只获取【用户】对象
        self.ou_search_filter = '(objectclass=organizationalUnit)'  # 只获取【OU】对象

    def users_get(self):
        """
        获取所有的用户
        :return:
        """
        self.conn.search(search_base='dc=testyun,dc=club', search_filter=self.search_filter, attributes=ALL_ATTRIBUTES)
        res = self.conn.response_to_json()
        res = json.loads(res)['entries']
        return res

    def ou_get(self):
        """
        获取所有的OU
        :return:
        """
        self.conn.search(search_base=self.active_base_dn, search_filter=self.ou_search_filter,
                         attributes=ALL_ATTRIBUTES)
        res = self.conn.response_to_json()
        res = json.loads(res)['entries']
        return res


if __name__ == '__main__':
    ad = SyncUtil()
    res = ad.users_get()

    for user in res:
        print('username:%s\tdn:%s' % (user['attributes']['sAMAccountName'], user['dn']))
