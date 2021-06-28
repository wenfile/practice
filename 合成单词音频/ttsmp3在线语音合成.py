import json
from os import path
import requests
import xlrd


def get_mp3(index, text):
    url = 'https://ttsmp3.com/makemp3_new.php'
    # headers = {
    #     'Connection': "keep-alive",
    #     'Content-type': "application/x-www-form-urlencoded",
    #     'Host': "ttsmp3.com",
    #     'Origin': 'https://ttsmp3.com',
    #     'Referer': 'https://ttsmp3.com/',
    #     'Sec-Fetch-Dest': 'empty',
    #     'Sec-Fetch-Mode': 'cors',
    #     'Sec-Fetch-Site': 'same-origin',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    # }
    data = {
        'msg': text,
        # 'lang': 'Joey',
        'lang': 'Matthew',
        # 'lang': 'Brian',
        'source': 'ttsmp3'
    }
    rest = requests.post(url, data=data)
    data = json.loads(rest.text)
    re_url = data["URL"]
    print(re_url)
    print(rest.status_code)
    filepath = path.dirname('C:/Users/fan/Desktop/衔接课词测录音频/L44-45/')  # 目录
    file = 'en{0}.mp3'.format(index)
    fout = open(filepath + '/' + file, 'wb')
    r = requests.get(re_url)
    fout.write(r.content)
    fout.close()
    print("output file '", filepath, file, "' success")


def read_excel():
    workbook = xlrd.open_workbook('C:/Users/fan/Desktop/12.xlsx')
    worksheet = workbook.sheets()[0]
    nrows = worksheet.nrows
    i = 79
    for row in range(79, nrows):
        r_data = worksheet.row_values(row)[0]
        i += 1
        get_mp3(i, r_data)
    print("over")


if __name__ == '__main__':
    read_excel()