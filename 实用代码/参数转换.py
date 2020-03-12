# 请求参数转换
headers = '''op: search
type: m
pageindex: 8
salestatus: 
baoben: 
currency: 
term: 
keyword: 
series: 01
risk: 
city: 
date: 
pagesize: 20
orderby: ord1
t: 0.9930362654056228
citycode: '''

headers = dict([line.split(": ",1) for line in headers.split("\n")])
print(headers)