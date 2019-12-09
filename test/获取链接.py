import requests
from bs4 import BeautifulSoup
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400'
}
url = 'https://v.qq.com/x/page/f0395fw1i3c.html'

res = requests.get(url,headers=headers)
res.encoding = 'utf-8'
suops = BeautifulSoup(res.text,'html.parser')

print(suops.text)