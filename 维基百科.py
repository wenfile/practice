import json
import random
import time

import requests
from lxml import html
import xlrd
import xlwt
from xlutils.copy import copy

"""维基百科——查询学校名"""


# 读取excel中学校名后缀
def get_university_en():
    data = xlrd.open_workbook("C:/Users/HFY/PycharmProjects/untitled1/美国大学.xlsx")
    table = data.sheets()[0]
    nrows = table.nrows  # 行数
    ncols = table.ncols  # 列数
    list_item = []
    for i in range(1, nrows):
        rowValues = table.row_values(i)  # 某一行数据bai
        for item in rowValues:
            list_item.append(item)
        print(list_item)
        list_item = []


# 获取维基百科信息
def get_wikipedia_info():
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    url = 'https://en.wikipedia.org/api/rest_v1/page/summary/Indiana University-Purdue University Indianapolis'
    requests.adapters.DEFAULT_RETRIES = 5  # 增加重连次数
    s = requests.session()
    s.keep_alive = False  # 关闭多余连接
    # time.sleep(random.randint(1, 5))
    rest = requests.get(
        url,
        headers={'User-Agent': user_agent}
    )
    data = json.loads(rest.text)
    print(data)



if __name__ == '__main__':
    # get_university_en()
    get_wikipedia_info()