from lxml import html


def parse():
    """ 将html文件中的内容，使用xpath进行解析"""
    # 读取文件中的内容
    f = open('../static/百度翻译.html', 'r', encoding='utf-8')
    s = f.read()

    selector = html.fromstring(s)
    # 解析得到英语
    span1 = selector.xpath('/html/body/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/a[1]/span/span/span/text()')
    print(span1[0])
    # 解析ul下面的内容
    ul1 = selector.xpath('/html/body/div[1]/div[5]/div[2]/div[2]/ul/li')
    print(len(ul1))
    for li in ul1:
        span2 = li.xpath('span')
        a1 = li.xpath('a/@href')
        if len(a1) > 0:
            print(a1[0])
        # print(span2)
    f.close()


if __name__ == '__main__':
    parse()
