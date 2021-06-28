import random
import time

import requests
from lxml import html
import xlrd
from xlutils.copy import copy


"""获取智课选校帝信息"""


# 获取学校信息
def get_school_info():
    arr_href = read_excel(5, 0, 16)
    print(len(arr_href))
    old_excel = xlrd.open_workbook('C:/Users/fan/Desktop/新加坡学校简介.xls')
    new_excel = copy(wb=old_excel)
    new_table = new_excel.get_sheet(0)
    old_table = old_excel.sheets()[0]
    nrows = old_table.nrows
    for row in arr_href:
        my_user_agent = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1Safari/534.50",
            "Moilla/5.0 (Windows; U; Windows NT 6.1; ) AppleWebKit/534.12 (KHTML, like Gecko)Maxthon/3.0 Safari/534.12",
            "Moilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; . NET CLR2.0.50727; . NET CLR 3.5.30729; . NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; . NET4.0C;. NET4.0E; SE 2.X MetaSr 1.0)",
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)',
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
            'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E) QQBrowser/6.9.11079.201',
            "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
            "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
        ]
        my_proxies = [
            'http: 115.218.214.43:9000',
            'http: 220.249.149.10:9999',
            'http: 113.195.170.60:9999',
            'http: 122.234.27.166:9000',
            'http: 39.108.92.182:8888',
            'http: 175.44.109.236:9999',
            'http: 125.108.72.108:9000',
            'http: 218.249.45.162:52316',
            'http: 36.248.133.22:9999',
            'http: 61.150.96.27:36880',
            'http: 112.111.217.38:9999',
        ]
        user_agent = random.choice(my_user_agent)
        proxie = random.choice(my_proxies)
        url = 'https://www.xuanxiaodi.com' + row
        print(url)
        headers = {
            'User-Agent': user_agent,
            'referer': url,
            'proxies': proxie,
            'Cookie': 'xxd_uid=1bf564dcb10c5c7386f3faaba7741a56; cpsInfo=%7B%22cookie_id%22%3A%2222cb4f30-d490-11ea-ae8e-e1caf62b51fd%22%2C%22first_time%22%3A%222020-08-02T07%3A16%3A51.235Z%22%2C%22hmsr%22%3A%22%22%2C%22hmmd%22%3A%22%22%2C%22hmpl%22%3A%22%22%2C%22hmkw%22%3A%22%22%2C%22hmci%22%3A%22%22%2C%22pid%22%3A%22%22%2C%22expires%22%3A%222030-07-31T07%3A16%3A51.235Z%22%7D; latestEntry=%7B%22cookie_id%22%3A%2222cb4f30-d490-11ea-ae8e-e1caf62b51fd%22%2C%22first_time%22%3A%222020-08-02T07%3A16%3A51.235Z%22%2C%22hmsr%22%3A%22%22%2C%22hmmd%22%3A%22%22%2C%22hmpl%22%3A%22%22%2C%22hmkw%22%3A%22%22%2C%22hmci%22%3A%22%22%2C%22pid%22%3A%22%22%2C%22expires%22%3A%222030-07-31T07%3A16%3A51.235Z%22%7D; xxd_referer=; io=_XDIuL6dcvGXmDKZAAAS; xxd_ticket=viSgkKfx5CoGRl2ShvIZjaQsiJiNG1y6; xxd_ticket.sig=YgCWYqmt6i0ummpTxRgO5RJoohE; xxd_user=%7B%22id%22%3A509379%2C%22userId%22%3A9601753%2C%22name%22%3A%22188****7839%22%2C%22avatarUrl%22%3A%22https%3A%2F%2Fmedia.xuanxiaodi.com%2Fuser%2Favatar%2Fdefault%2F1e%2F6a%2F1e6a4fc891f5debe8523188d39e929ae5a7f.jpg%22%7D; xxd_user.sig=5fdAeWT3k4s227CCIoqolDMBFhU; xxd_previous=%7B%22title%22%3A%22%E7%BA%BD%E7%BA%A6%E5%A4%A7%E5%AD%A6%E7%AE%80%E4%BB%8B%22%2C%22url%22%3A%22https%3A%2F%2Fwww.xuanxiaodi.com%2Fschool%2F963%2Fdetail%2Fintroduction%22%2C%22timestamp%22%3A1598186610399%7D'
        }
        requests.adapters.DEFAULT_RETRIES = 5  # 增加重连次数
        s = requests.session()
        s.keep_alive = False  # 关闭多余连接
        ht = s.get(url, headers=headers)
        time.sleep(random.randint(5, 10))
        html_data = ht.text
        print(ht.status_code)
        selector = html.fromstring(html_data)
        # 头部信息
        # arr_logo_url = []
        # arr_cnname = []
        # arr_enname = []
        # arr_addr = []
        # arr_web = []
        # list1 = selector.xpath('//div[@class="section-left pull-left"]/div[@class="school-info-box clearfix"]')
        # print(len(list1))
        # for l1 in list1:
        #     # logo
        #     logo = l1.xpath('div[@class="school-logo pull-left"]/div/div/img/@src')
        #     print(logo)
        #     arr_logo_url.append(logo[0])
        #     # 中文名
        #     cn_name = l1.xpath('div[@class="school-text pull-left"]/h1/text()')
        #     arr_cnname.append(cn_name[0])
        #     # 英文名
        #     en_name = l1.xpath('div[@class="school-text pull-left"]/h2/text()')
        #     if len(en_name) > 0:
        #         arr_enname.append(en_name[0])
        #     # 地址
        #     address = l1.xpath('div[@class="school-text pull-left"]/div[@class="school-location"]/span/text()')
        #     arr_addr.append(address[0])
        #     # 网址
        #     website = l1.xpath('div[@class="school-text pull-left"]/div[@class="school-website"]/a/@href')
        #     arr_web.append(website[0])
        # logo_url = ''.join(arr_logo_url)
        # cnname = ''.join(arr_cnname)
        # enname = ''.join(arr_enname)
        # addr = ''.join(arr_addr)
        # web = ''.join(arr_web)
        # print(logo_url)
        # print(cnname)
        # print(enname)
        # print(addr)
        # print(web)

        # list2 = selector.xpath('//div[@class="section-right pull-right"]/div[@class="rank-box clearfix"]')
        # arr_country_rank = []
        # arr_world_rank = []
        # for l2 in list2:
        #     # 国家排名
        #     rank_main1 = l2.xpath('//div[@class="rank-item pull-left"][1]/div[@class="rank-main"]')
        #     usnews_country_rank = rank_main1[0].xpath('string()')
        #     arr_country_rank.append(usnews_country_rank)
        #     # print(usnews_country_rank)
        #     rank_sub1 = l2.xpath('//div[@class="rank-item pull-left"][1]/div[@class="rank-sub"]')
        #     if len(rank_sub1) > 0:
        #         qs_country_rank = rank_sub1[0].xpath('string()')
        #         arr_country_rank.append(qs_country_rank)
        #         # print(qs_country_rank)
        #     if len(rank_sub1) > 1:
        #         the_country_rank = rank_sub1[1].xpath('string()')
        #         arr_country_rank.append(the_country_rank)
        #         # print(the_country_rank)
        #
        #     # 世界排名
        #     rank_main2 = l2.xpath('//div[@class="rank-item pull-left"][2]/div[@class="rank-main"]')
        #     usnews_world_rank = rank_main2[0].xpath('string()')
        #     arr_world_rank.append(usnews_world_rank)
        #     # print(usnews_world_rank)
        #     rank_sub1 = l2.xpath('//div[@class="rank-item pull-left"][2]/div[@class="rank-sub"]')
        #     if len(rank_sub1) > 0:
        #         qs_world_rank = rank_sub1[0].xpath('string()')
        #         arr_world_rank.append(qs_world_rank)
        #         # print(qs_world_rank)
        #     if len(rank_sub1) > 1:
        #         the_world_rank = rank_sub1[1].xpath('string()')
        #         arr_world_rank.append(the_world_rank)
        #         # print(the_world_rank)
        # str_country_rank = ';'.join(arr_country_rank)
        # str_world_rank = ';'.join(arr_world_rank)
        # print(str_country_rank)
        # print(str_world_rank)

        # 标题
        list2 = selector.xpath('//div[@class="school-title-name"]')
        title = list2[0].xpath('string()') if len(list2) > 0 else None
        print(title)

        # 学校简介1
        list3 = selector.xpath('//div[@class="section-item section-school-brief"]/div[@class="pc-container"]/'
                               'div[@class="section-inner-box"]/div[@class="section-item-content"]/div[@class="brief-box clearfix"]'
                               '/div[@class="brief-item pull-left"]')
        arr_brief1 = []
        for l3 in list3:
            brief1 = l3.xpath('string()')
            arr_brief1.append(brief1)
        str_brief1 = '、'.join(arr_brief1).replace('录取率', '录取率-').replace('申请人数', '申请人数-').replace('毕业率', '毕业率-').replace('就业率', '就业率-').\
            replace('毕业薪资', '毕业薪资-').replace('国际学生比例', '国际学生比例-').replace('学生总数量', '学生总数量-').replace('本科生数量', '本科生数量-').\
            replace('研究生数量', '研究生数量-').replace('师生比例', '师生比例-').replace('男女比例', '男女比例-').replace('更多', '').replace('中期薪资', '；中期薪资').\
            replace('\n', '').strip()
        print(str_brief1)

        # 学校简介2
        arr_brief2 = []
        list4 = selector.xpath('//div[@class="section-item section-school-brief"]//div[@class="component-rich-text brief-desc"]/span[@class="content"]/p')
        print(len(list4))
        for l4 in list4:
            brief2 = l4.xpath('string()')
            arr_brief2.append(brief2)
        str_brief2 = '\n'.join(arr_brief2)
        print(str_brief2)

        # 强势专业
        arr_strong_professional = []
        list5 = selector.xpath('//div[@class="section-item section-major"][1]/div/div/div[@class="section-item-content"]/div/div')
        for l5 in list5:
            strong_professional = l5.xpath('string()')
            arr_strong_professional.append(strong_professional)
        str_strong_professional = '、'.join(arr_strong_professional)
        print(str_strong_professional)

        # 热门专业
        arr_popular_major = []
        list6 = selector.xpath('//div[@class="section-item section-major"][2]/div/div/div[@class="section-item-content"]/div/div')
        for l6 in list6:
            popular_major = l6.xpath('string()')
            arr_popular_major.append(popular_major)
        str_popular_major = '、'.join(arr_popular_major)
        print(str_popular_major)

        # 图片链接
        arr_image_url = []
        list7 = selector.xpath('//div[@class="school-images-list"]/div/div[@class="slick-list"]/div[@class="slick-track"]//div[@class="image-preload white-bg"]')
        print(len(list7))
        for l7 in list7:
            image_url = l7.xpath('img/@src')
            if image_url[0] not in arr_image_url:
                arr_image_url.append(image_url[0])
        str_image_url = '、'.join(arr_image_url)
        print(str_image_url)

        # 其他介绍
        item_head = selector.xpath('//div[@class="container-school-introduction-detail"]/div[@class="section-item"]//div[@class="section-item-head"]/text()')
        print(item_head)
        arr_item_content = []
        item_content = selector.xpath('//div[@class="container-school-introduction-detail"]/div[@class="section-item"]//div[@class="section-item-content"]//'
                                   'span[@class="content"]')
        for item in item_content:
            item_content = item.xpath('p/text()')
            item_content = '\n'.join(item_content)
            arr_item_content.append(item_content)
        print(arr_item_content)
        i = 0
        for item in item_head:
            if item == '选择该校的理由':
                if '2、' not in arr_item_content[i]:
                    content = arr_item_content[i]
                    new_table.write(nrows, 12, content[2:])
                else:
                    new_table.write(nrows, 12, arr_item_content[i])
            elif item == '地理位置':
                new_table.write(nrows, 13, arr_item_content[i])
            elif item == '学校历史':
                new_table.write(nrows, 14, arr_item_content[i])
            elif item == '校园环境':
                new_table.write(nrows, 15, arr_item_content[i])
            elif item == '学校特色':
                new_table.write(nrows, 16, arr_item_content[i])
            elif item == '院系设置':
                new_table.write(nrows, 17, arr_item_content[i])
            elif item == '教学特色':
                new_table.write(nrows, 18, arr_item_content[i])
            elif item == '学校住宿':
                new_table.write(nrows, 19, arr_item_content[i])
            elif item == '图书馆':
                new_table.write(nrows, 20, arr_item_content[i])
            elif item == '学校设施':
                new_table.write(nrows, 21, arr_item_content[i])
            elif item == '好评项':
                new_table.write(nrows, 22, arr_item_content[i])
            elif item == '差评项':
                new_table.write(nrows, 23, arr_item_content[i])
            i += 1

        # 招生办信息
        arr_admission_content = []
        list_admission_content = selector.xpath('//div[@class="container-school-introduction-detail"]/div[@class="section-item section-admission-office"]//'
                                                'span[@class="content"]/p')
        for l in list_admission_content:
            admission_content = l.xpath('string()')
            arr_admission_content.append(admission_content)
        str_admission = ''.join(arr_admission_content).replace('地址', '\n地址').replace('邮箱', '\n邮箱').replace('电话', '\n电话').\
            replace('传真', '\n传真').replace('在线申请', '\n在线申请').replace('硕士招办联系方式', '\n硕士招办联系方式').replace('博士招办联系方式', '\n博士招办联系方式').\
            replace('MBA招办联系方式', '\nMBA招办联系方式').replace('语言中心招办联系方式', '\n语言中心招办联系方式').replace('研究生证书与文凭招办联系方式', '\n研究生证书与文凭招办联系方式').\
            replace('专科招办联系方式', '\n专科招办联系方式').replace('预科招办联系方式', '\n预科招办联系方式').replace('网址', '\n网址').replace('邮件', '\n邮件')\
            .strip()
        new_table.write(nrows, 24, str_admission)

        # 写入excel
        # new_table.write(nrows, 0, logo_url)
        # new_table.write(nrows, 1, cnname)
        # new_table.write(nrows, 2, enname)
        # new_table.write(nrows, 3, addr)
        # new_table.write(nrows, 4, web)
        # new_table.write(nrows, 5, str_country_rank)
        # new_table.write(nrows, 6, str_world_rank)
        new_table.write(nrows, 6, title)
        new_table.write(nrows, 7, str_brief1)
        new_table.write(nrows, 8, str_brief2)
        new_table.write(nrows, 9, str_strong_professional)
        new_table.write(nrows, 10, str_popular_major)
        new_table.write(nrows, 11, str_image_url)
        nrows += 1
        new_excel.save('C:/Users/fan/Desktop/新加坡学校简介.xls')



# 读取excel中url后缀
def read_excel(sheet_num, num1, num2):
    r_url_list = []
    i = 0
    workbook = xlrd.open_workbook('C:/Users/fan/Desktop/选校帝链接.xlsx')
    worksheet = workbook.sheets()[sheet_num]
    for row in worksheet.get_rows():
        r_url = row[0].value
        if num1 <= i <= num2:
            r_url_list.append(r_url)
        i += 1
    return r_url_list


# 获取学校链接
def get_href():
    old_excel = xlrd.open_workbook('C:/Users/HFY/Desktop/智课选校帝链接.xls')
    new_excel = copy(wb=old_excel)
    new_table = new_excel.get_sheet(5)
    old_table = old_excel.sheets()[5]
    nrows = old_table.nrows
    ncols = old_table.ncols
    for num in range(1, 2):
        url = 'https://www.xuanxiaodi.com/schools/187-0-0-0-0-0-1.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
        requests.adapters.DEFAULT_RETRIES = 5  # 增加重连次数
        s = requests.session()
        s.keep_alive = False  # 关闭多余连接
        s.proxies = {"http": "113.194.28.99:9999"}
        html_data = s.get(url, headers=headers)
        time.sleep(10)
        print(html_data.status_code)
        html_data = html_data.text
        selector = html.fromstring(html_data)
        li_list = selector.xpath('//div[@class="schools-box"]/ul[@class="school-list"]/div[@class="component-school-item "]/div[@class="info-box"]/div[@class="top-box"]')
        print(len(li_list))
        for li in li_list:
            href = li.xpath('a/@href')[0]
            print(href)
            new_table.write(nrows, 0, href)
            nrows += 1
    new_excel.save('C:/Users/HFY/Desktop/智课选校帝链接.xls')


if __name__ == '__main__':
    # get_href()
    get_school_info()