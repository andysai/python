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
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

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



print(res_movie.status_code)