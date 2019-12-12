import scrapy
import bs4
from ..items import DangdangwangItem

class DangdangwangSpider(scrapy.Spider):
    name = 'dangdangwang'
    allowed_domains = ['http://bang.dangdang.com']
    url_lists = []
    for i in range(3):
        url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2018-0-1-' + str(i + 1)
        url_lists.append(url)
    print('1')

    def parse(self, response):
        print('2')
        datas = bs4.BeautifulSoup(response.text,'html.parser').find('ul',class_='bang_list clearfix bang_list_mode').find_all('li')
        for data in datas:
            item = DangdangwangItem()
            item['name'] = data.find('div', class_="name").find('a')['title']
            item['author'] = data.find('div', class_="publisher_info").text
            item['price'] = data.find('div', class_="price").find('span', class_="price_n").text

            yield item
        print('3')
