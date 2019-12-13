# -*- coding: utf-8 -*-
import csv
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class JobuiPipeline(object):
    def process_item(self, item, spider):
        f = open('./storage/data/%(name)s.csv','a+',newline='')
        writer = csv.writer(f)
        writer.writerow(["招聘公司名","招聘职位","工作地点","条件要求"])
        writer.writerow((item['company'],item['job'],item['address'],item['conditions']))
        return item
        
