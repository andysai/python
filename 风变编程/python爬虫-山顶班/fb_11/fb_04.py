# 项目目标：使用多协程和队列，爬取时光网电视剧TOP100的数据（剧名、导演、主演和简介），并用csv模块将数据存储下来。
# 时光网TOP100链接：http://www.mtime.com/top/tv/top100/
#提示：
#1.分析数据存在哪里（打开“检查”工具，刷新页面，查看第0个请求，看【response】）
#2.观察网址规律（多翻几页，看看网址会有什么变化）
#3.获取、解析和提取数据（需涉及知识点：queue、gevent、request、BeautifulSoup、find和find_all）
#4.存储数据（csv本身的编码格式是utf-8，可以往open（）里传入参数encoding='utf-8'。这样能避免由编码问题引起的报错。)
#注：在练习的【文件】中，你能找到自己创建的csv文件。将其下载到本地电脑后，请用记事本打开，因为用Excel打开可能会因编码问题出现乱码。
from gevent import monkey
monkey.patch_all()
import requests,time,csv,gevent
from bs4 import BeautifulSoup
from gevent.queue import Queue


# 添加请求头
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh,zh-CN;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6,zh-HK;q=0.5',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '_userCode_=20191272346265901; _userIdentity_=20191272346264157; _tt_=821EF180C19DF98BCCF469F73DB1D69A; __utmz=196937584.1575733587.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); DefaultCity-CookieKey=364; DefaultDistrict-CookieKey=0; _ydclearance=333525a9207dab7f7264599a-06f8-4ec6-b4a1-9dcaba5ddba6-1575907320; __utma=196937584.1593013846.1575733587.1575733587.1575900120.2; __utmt=1; __utmt_~1=1; maxShowNewbie=1; yd_cookie=4b488d94-05d9-4ba5893b50b63689a56315fdfa7ff891a9a4; __utmc=196937584; Hm_lvt_6dd1e3b818c756974fb222f0eae5512e=1575733587,1575900121,1575900921; homePageType=B; userId=0; defaultCity=%25E5%25B9%25BF%25E4%25B8%259C%257C364; strIdCity=China_Beijing; __utmb=196937584.26.10.1575900120; Hm_lpvt_6dd1e3b818c756974fb222f0eae5512e=1575901246',
    'Host': 'www.mtime.com',
    'Referer': 'http://www.mtime.com/top/tv/top100/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}


# 添加TOP100电视剧的链接
url_lists = []
for i in range(1,11):
    if i == 1:
        url = 'http://www.mtime.com/top/tv/top100/'
    else:
        url = 'http://www.mtime.com/top/tv/top100/' + 'index-' + str(i) + '.html'
    url_lists.append(url)

url_1 = 'http://www.mtime.com/top/tv/top100/'
res_movie = requests.get(url_1,headers=headers)
suop_movies = BeautifulSoup(res_movie.text,'html.parser').find('div',class_='top_list').find_all('li')
for suop_movie in suop_movies:
    name = suop_movie.find(class_='px14 pb6')
    actor = suop_movie.find_all('p')[0]
    actor1 = suop_movie.find_all('p')[1]
    print(actor.text,actor1.text)