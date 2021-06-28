import requests
from lxml import html

def spider(sn):
    url = 'http://search.dangdang.com/?key={sn}&act=input'.format(sn=sn)
    # 获取html
    html_data = requests.get(url).text

    # xpath对象
    selector = html.fromstring(html_data)

    # 找到书本列表
    ul_list = selector.xpath('//div[@id="search_nature_rg"]/ul/li')
    print(len(ul_list))
    index = 0
    for li in ul_list:
        index += 1
        # 标题
        title = li.xpath('a/@title')
        print(str(index) + title[0])
        # 链接
        link = li.xpath('a/@href')
        print(link[0])
        # 价格
        price = li.xpath('p[@class="price"]/span[@class="search_now_price"]/text()')
        price = '无' if len(price) == 0 else price[0]
        print(price.replace('¥', ''))
        # 缩略图
        image = li.xpath('a[@class="pic"]/img/@alt')
        print(image[0])


if __name__ == '__main__':
    spider('%C8%CB%C0%E0%BC%F2%CA%B7')