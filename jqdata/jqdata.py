#!/usr/bin/env python3

from jqdatasdk import *
import json

# 从access.json中获取帐号与密码
access_file = open('./access.json')
access_data = access_file.read()
user_info = json.loads(access_data)

# 初始化JQData接口
auth(user_info['username'], user_info['password'])
is_auth = is_auth()

# 查询剩余可用数据条数
query_count = get_query_count()

print(query_count)
