import time,requests,schedule,smtplib
from email.mime.text import MIMEText
from email.header import Header
from bs4 import BeautifulSoup

headers={
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
url = 'http://www.xiachufang.com/explore/'
res = requests.get(url,headers=headers)
suops = BeautifulSoup(res.text,'html.parser').find('div',class_='normal-recipe-list')

print(suops)