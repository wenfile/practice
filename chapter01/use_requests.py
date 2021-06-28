import requests


def get_book():
    url = 'http://search.dangdang.com'
    rest = requests.get(url, params={
        'key': '%C8%CB%C0%E0%BC%F2%CA%B7',
        'act': 'input'
    })
    # print(rest.text)
    # print(rest.status_code)
    po = requests.post(url)
    print(po.text)

if __name__ == '__main__':
    get_book()