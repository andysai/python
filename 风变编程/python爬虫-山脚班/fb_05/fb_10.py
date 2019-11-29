# 导入模块
import requests
import random

# 快递网站连接
URL = 'https://www.kuaidi100.com/query?'
# 输入需要查询的物流公司:
wl_company = input('请输入需要查询的物流公司:')
# 输入需要查询的快递单号
kuaidi_number = input('请输入需要查询的快递单号:')
# 请输入浏览器上cookie值
cookie = input('请输入网页的cookie值:')

# 伪装
headers = {
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.kuaidi100.com/',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': cookie,
    'Host': 'www.kuaidi100.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400',
    'X-Requested-With': 'XMLHttpRequest'
}
a = random.random()
# 将参数封装为字典
params = {'type': wl_company, 'postid': kuaidi_number, 'temp': a, 'phone': ''}

res = requests.get(URL,params=params,headers=headers)
lists = res.json()
for list in lists['data']:
    print(list['context'])
