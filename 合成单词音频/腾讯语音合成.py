import time
from os import path
from urllib.request import urlopen
from urllib.parse import urlencode
from urllib.parse import quote_plus
import hashlib
import random
import base64
import xlrd


# 生成sign
def getReqSign(params, key):
    dict_kl = sorted(params)
    s = ''
    for k in dict_kl:
        v = params[k]
        if v != '':
            v0 = str(quote_plus(str(v)))
            s = s + k + '=' + v0 + '&'
    s = s + 'app_key=' + key
    m = hashlib.md5()
    m.update(s.encode("utf8"))
    sign = m.hexdigest()
    sign = sign.upper()
    print('sign:', sign)
    return sign


def get_request(index, text):
    appid = '2159973522'
    appkey = 'JVbXxDHYh0CNdFhQ'
    url = 'https://api.ai.qq.com/fcgi-bin/aai/aai_tts'
    time_s = int(time.time())
    m = hashlib.md5()
    m.update(str(time_s).encode("utf8"))
    nonce_s = m.hexdigest()
    nonce_s = nonce_s[0:random.randint(1, 31)]
    params = {'app_id': appid,
              'speaker': '1',
              'format': '3',
              'volume': '5',
              'speed': '100',
              'text': text,
              'aht': '0',
              'apc': '58',
              'time_stamp': time_s,
              'nonce_str': nonce_s,
              'sign': ''
              }
    params['sign'] = getReqSign(params, appkey)
    s = urlencode(params)
    res = urlopen(url, s.encode())  # 网络请求
    res_str = res.read().decode()
    res_dict = eval(res_str)
    print('return result : ')
    print('ret:', res_dict['ret'])
    print('msg:', res_dict['msg'])
    time.sleep(1)
    if res_dict['ret'] == 0:
        res_data = res_dict['data']
        res_data_format = res_data['format']
        res_data_speech = res_data['speech']
        res_data_md5sum = res_data['md5sum']
        filepath = path.dirname('C:/Users/HFY/Desktop/zh/')  # 目录
        file = 'zh{0}.mp3'.format(index)
        base64_data = res_data_speech
        ori_image_data = base64.b64decode(base64_data)
        fout = open(filepath + '/' + file, 'wb')
        fout.write(ori_image_data)
        fout.close()
        print("output file '", filepath, file, "' success")


def read_excel():
    workbook = xlrd.open_workbook('C:/Users/HFY/Desktop/12.xlsx')
    worksheet = workbook.sheets()[0]
    i = 0
    for row in worksheet.get_rows():
        r_data = row[0].value
        i += 1
        get_request(i, r_data)
    print('over')


if __name__ == '__main__':
    read_excel()