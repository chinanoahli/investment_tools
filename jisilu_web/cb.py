#!/usr/bin/env python3

# 下载地址及使用说明
# https://github.com/chinanoahli/investment_tools

# 遇到问题请提Issues
# 或给我发邮件（不保证全都能解决）：10005128+chinanoahli@users.noreply.github.com

from time import gmtime, strftime
from pandas.io.json import json_normalize
from urllib.request import urlopen, Request
import calendar
import platform
import pandas
import time
import json
import os

# 设置pandas输出格式（终端），不限制最大列数，不限制最大行数，不限制显示宽度，数字保留3位小数
pandas.set_option ('display.max_columns', None)
pandas.set_option ('display.max_rows', None)
pandas.set_option ('display.width', None)
pandas.options.display.float_format = '{:.3f}'.format

# 获取当前时间
now_time = calendar.timegm(time.gmtime())
now_time_int = int(now_time)
now_time_str = str(now_time_int)

# 拼接请求地址
url = 'https://www.jisilu.cn/data/cbnew/cb_list/?___jsl=LST___t=' + now_time_str

# 请求数据
web_data = urlopen(Request(url,\
        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}))

data_str = web_data.read().decode('utf-8')

data_downloaded = json.loads(data_str)
data_dic = data_downloaded ['rows']
data_df = json_normalize(data_dic)

# 定义需要用到的列
column_list = ['cell.pre_bond_id', 'cell.bond_nm', 'cell.stock_id', 'cell.stock_nm',\
        'cell.convert_price', 'cell.convert_dt', 'cell.maturity_dt', 'cell.next_put_dt',\
        'cell.put_convert_price', 'cell.redeem_dt', 'cell.redeem_flag', 'cell.rating_cd',\
        'cell.force_redeem', 'cell.real_force_redeem_price', 'cell.force_redeem_price',\
        'cell.premium_rt', 'cell.year_left', 'cell.ytm_rt_tax', 'cell.price',\
        'cell.convert_cd_tip', 'cell.price_tips']

columns_needs = [i for i in data_df.columns if i in column_list]

# 提取需要用到的数据
cb_data = data_df[columns_needs]

# 设置评级过滤条件（修改时请注意将输入法调整到英文输入模式，符号和文字必须是半角英语字符）
credit_list = ['AAA', 'AAA-', 'AAA+', 'AA', 'AA+']

# 剔除非上述条件的转债
cb_data = cb_data[cb_data['cell.rating_cd'].isin(credit_list)]

# 替换中文列名
data_output = cb_data.rename(columns={'cell.pre_bond_id': '转债代码', 'cell.bond_nm': '转债名称',\
        'cell.stock_id': '正股代码', 'cell.stock_nm': '正股名称', 'cell.convert_price': '转股价',\
        'cell.convert_dt': '转股起始日', 'cell.maturity_dt': '到期日', 'cell.next_put_dt': '回售起始日',\
        'cell.put_convert_price': '回售触发价', 'cell.redeem_dt': '强赎执行日', 'cell.redeem_flag': '公布强赎',\
        'cell.rating_cd': '评级', 'cell.force_redeem': '强赎提醒', 'cell.real_force_redeem_price': '强赎价格',\
        'cell.force_redeem_price': '强赎触发价', 'cell.premium_rt': '溢价率', 'cell.year_left': '剩余到期年限',\
        'cell.ytm_rt_tax': '到期税后收益', 'cell.price': '转债现价', 'cell.convert_cd_tip': '转股提示',\
        'cell.price_tips': '现价提示'}, inplace=False)

# 获取当前系统时间，作为文件名时间戳
timestamp = strftime('%Y%m%d%H%M%S', gmtime())

# 获取桌面路径并拼接生成文件名
desktop_path = os.path.normpath(os.path.expanduser('~/Desktop'))
output_filename = desktop_path + '/cb_' + timestamp + '.csv'

# 获取系统类型，Windows: 将文件编码设为gb18030，Linux和Mac: 将文件编码设为utf-8
system_platform = platform.system()
if (system_platform == 'Linux') or (system_platform == 'Darwin'):
    output_encoding = 'utf-8'
elif (system_platform == 'Windows'):
    output_encoding = 'gb18030'

# 输出数据到当前目录的'cb_时间戳.csv'文件
data_output.to_csv(output_filename, encoding=output_encoding, index=False)

# 输出数据到终端
print(data_output)

print('==========  ==========')

# 脚本执行完成提示
print('已将数据输出到 ' + output_filename + ' 文件，文件编码是' + output_encoding + '，请用Excel或WPS打开文件')

print('请按回车(Enter / Return)键退出...')

input()
