import openpyxl

class JobuiPipeline(object):
    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.append(['公司', '职位', '地址', '招聘信息'])

    def process_item(self,item,spider):
        line = [ item['company_name'],item['position'],item['place'],item['rr']]
        self.ws.append(line)
        return item

    def close_spider(self,spider):
        self.wb.save('test.csv')
        self.wb.close()