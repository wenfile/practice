import requests
from lxml import html


def spider():
    """ 爬取京东的图书数据 """
    url = 'https://club.jd.com/comment/productCommentSummaries.action?referenceIds=66847265611'
    # 获取html文档
    html_doc = requests.get(url).json()
    print(html_doc)
    # 获取xpath对象

    # 找到列表的集合

    # 解析对应的内容
    # 书名


if __name__ == '__main__':
    spider()