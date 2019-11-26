#  序号/电影名/评分/推荐语/链接
import requests,random
from bs4 import BeautifulSoup

for x in range(10):
    URL = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    # URL = 'https://movie.douban.com/top250?start=0&filter='
    res = requests.get(URL)
    suop = BeautifulSoup(res.text,'html.parser')
    web = suop.find('ol',class_='grid_view')
print(res.status_code)