import json
import requests
from lxml import html
import xlrd


def get_request():
    words = read_excel()
    for word in words:
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
        url = 'https://dictionary.cambridge.org/dictionary/english-chinese-simplified/{0}'.format(word)
        requests.adapters.DEFAULT_RETRIES = 5  # 增加重连次数
        s = requests.session()
        s.keep_alive = False  # 关闭多余连接
        html_data = requests.get(
            url,
            headers={'User-Agent': user_agent}
        ).text
        selector = html.fromstring(html_data)
        div_list = selector.xpath('//article[@id="page-content"]/div[@class="pr di superentry"]//div[@class="entry-body"]//div[@class="def-block ddef_block "]')
        result = ''
        for div in div_list:
            content = div.xpath('string()')
            content = content.splitlines()
            for tt in content:
                tt = tt.strip()
                if tt:
                    result += tt + '\n'
        result = word + '\n' + result + '\n' + '__________________________'
        print(result)


def read_excel():
    workbook = xlrd.open_workbook('C:/Users/fan/Desktop/工作簿1.xlsx')
    worksheet = workbook.sheets()[0]
    words = []
    for row in worksheet.get_rows():
        word = row[0].value
        words.append(word)
    return words


if __name__ == '__main__':
    get_request()
    # read_excel()