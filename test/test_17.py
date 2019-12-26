import requests,time
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400'
}

for i in range(3):
    data = {
        'op': 'search',
        'type': 'm',
        'pageindex': '8',
        'salestatus': '',
        'baoben': '',
        'currency': '',
        'term': '',
        'keyword': '',
        'series': '01',
        'risk': '',
        'city': '',
        'date': '',
        'pagesize': '20',
        'orderby': 'ord1',
        't': '0.9930362654056228',
        'citycode': ''
    }
    url = 'http://www.cmbchina.com/cfweb/svrajax/product.ashx?op=search&type=m&pageindex=' + str(i) + '&salestatus=&baoben=&currency=&term=&keyword=&series=01&risk=&city=&date=&pagesize=20&orderby=ord1&t=0.9930362654056228&citycode='
    res = requests.get(url)
    res.encoding = 'utf-8'
    suop = BeautifulSoup(res.text,'html.parser')
    print(suop)