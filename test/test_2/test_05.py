import requests
from bs4 import BeautifulSoup



def _introduce():
    mac_address = 'b40b.44ce.69c7'

    mac_address_list = []

    for i in mac_address:
        mac_address_list.append(i)

    mac_address_list[2:0] = '-'
    mac_address_list[8:0] = '-'
    mac_address_list[14:0] = '-'
    mac_address_str = "".join(str(i) for i in mac_address_list).replace('.', '-')
    return mac_address_str


def get_organization():
    url = 'https://mac.51240.com/' + _introduce() + '__mac/'
    print(url)
    headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        # 标记了请求从什么设备，什么浏览器上发出
        }
    res = requests.get(url,headers=headers)
    mes = res.status_code # 查看网页状态
    suop = BeautifulSoup(res.text,'html.parser')
    web = suop.find_all('tr')
    message = []
    for tr in web:
        num = tr.find('td', bgcolor='#FFFFFF').text
        if num not in message:
            message.append(num)

    print(f'mac地址为:{message[0]}\n组织名称为:{message[1]}')
get_organization()