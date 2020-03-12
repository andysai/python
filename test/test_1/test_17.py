import requests,time
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400'
}

url = 'https://www.993dy.com/vod-detail-id-13129.html'

res_url = requests.get(url,headers=headers)
print(res_url.status_code)
res_url.encoding = 'utf-8'
suop_urls = BeautifulSoup(res_url.text,'html.parser').find('ul',class_='downurl').find('script') # .find_all('div',class_='dwon_xl')
print(suop_urls)
#for i in suop_urls:
#    link = i.find_all('div',class_='dwon_xl')
    #print(link)

