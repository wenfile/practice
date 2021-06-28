import requests
from lxml import html
import xlrd
from xlutils.copy import copy
import json


def abbr(key):
    html_doc = requests.get('https://www.abbreviations.com/abbreviation/{0}'.format(key)).text
    selector = html.fromstring(html_doc)
    tr_list = selector.xpath('//*[@id="content-body"]/div/div[3]/div[@class="tdata-ext col-sm-12"]/'
                             'table[@class="table tdata no-margin"]/tbody/tr/td[@class="tal tm fsl"]')
    i = len(tr_list)
    if i == 0:
        print('空')
        return None
    else:
        while i > 0:
            result = []
            for td in tr_list:
                t1 = td.xpath('a/text()')
                if t1[0] not in result:
                    result.append(t1[0])
            i = i - 1
            new_result = ' '.join(result)
        print(new_result)
        return new_result


def get_request():
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    url = 'https://www.usnews.com/education/best-global-universities/rankings?format=json&page=12'
    # rest = requests.get(url, params={
    #     '_id':'5e4b6dbde018b67425258d9f',
    #     't':'1592225792524'
    # })
    rest = requests.get(
        url,
        headers={'User-Agent': user_agent}
    )
    dict = json.loads(rest.text)
    items = dict['items']
    for item in items:
        print(item['city'])


def r_excel():
    old_excel = xlrd.open_workbook('C:/Users/fan/Desktop/abbr.xlsx')
    sheet = old_excel.sheets()[0]
    i = 0
    new_excel = copy(old_excel)
    for row in sheet.get_rows():
        data = row[0].value
        text = abbr(data)
        ws = new_excel.get_sheet(0)
        ws.write(i, 1, text)
        new_excel.save('abbr.xls')
        old_excel = xlrd.open_workbook('abbr.xls')
        new_excel = copy(old_excel)
        i = i + 1
    print('全部写入完成')


if __name__ == '__main__':
    # r_excel()
    get_request()