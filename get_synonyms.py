import random
import MySQLdb
import requests
from lxml import html
import xlrd


# 获取同义词并生成4个选项
def get_conn():
    """获取mysql的连接"""
    conn = MySQLdb.connect(
        db='vocabulary',
        host='localhost',
        user='root',
        password='',
        charset='utf8'
    )
    return conn


def read_excel():
    excel = xlrd.open_workbook('C:/Users/fan/Desktop/33.xlsx')
    sheet = excel.sheets()[0]
    arr = []
    for row in sheet.get_rows():
        data = row[0].value
        arr.append(data)
    # print(arr)
    return arr


def get_skl():
    conn = get_conn()
    cursor = conn.cursor()

    arr = read_excel()
    for key in arr:
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
        url = 'https://www.collinsdictionary.com/zh/dictionary/english-thesaurus/{0}'.format(key)
        headers = {'User-Agent': user_agent}

        requests.adapters.DEFAULT_RETRIES = 5  # 增加重连次数
        s = requests.session()
        s.keep_alive = False  # 关闭多余连接
        s.proxies = {"http": "59.37.18.243:3128", "http": "123.207.43.128:1080", "http": "58.250.21.56:3128",
                     "http": "139.199.153.25:1080",
                     "http": "112.74.86.42:80"}
        r = s.get(
            url,
            headers=headers
        )
        html_data = r.text
        selector = html.fromstring(html_data)
        div_list = selector.xpath('//*[@id="main_content"]//div[@class="content synonyms dictionary thesbase"]/div[@class="hom"]/div[1]//div[@class="blockSyn"]/div')
        # print(len(div_list))
        syn_word = []
        sat_word = []
        for div in div_list:
            syn = div.xpath('a/span/text()')
            syn = "".join(syn)
            # print(syn)
            sql = 'SELECT * FROM `sat_vocabulary_1600` WHERE `en`="{0}"'.format(syn)
            cursor.execute(sql)
            data = cursor.fetchall()
            if data:
                sat_word.append(data[0][1])
            if syn:
                syn_word.append(syn)
        # print(syn_word)
        # print(sat_word)
        # 从列表中获取1一个随机单词
        if sat_word:
            answer_key = random.sample(sat_word, 1)
        if syn_word:
            answer_key = random.sample(syn_word, 1)
    # print('答案：', answer_key)
        # 从表balang_vocabulary_3500随机取得3个单词
        i = 0
        xuanxiang = []
        while i < 3:
            index = random.sample(range(0, 3397), 1)[0]
            # print(type(index))
            sql = 'SELECT en FROM `balang_vocabulary_3500` WHERE `id`={0}'.format(index)
            cursor.execute(sql)
            data_en = cursor.fetchall()
            i = i + 1
            data_en = list(data_en[0])
            xuanxiang.append(data_en)
        # print(len(xuanxiang))
        # 将答案随机插入到选项列表中
        str_xuangxiang = ''
        i = random.randint(0, len(xuanxiang))
        xuanxiang.insert(i, answer_key)
        for row in xuanxiang:
            str_xuangxiang += str(row[0]) + '\t'
        answer = {
            0: 'A',
            1: 'B',
            2: 'C',
            3: 'D'
        }
        print(str_xuangxiang, answer[i])
    cursor.close()
    conn.close()


if __name__ == '__main__':
    get_skl()