# 请求参数转换
headers = '''ct: 24
qqmusic_ver: 1298
new_json: 1
remoteplace: txt.yqq.center
searchid: 39853066037619909
t: 0
aggr: 1
cr: 1
catZhida: 1
lossless: 0
flag_qc: 0
p: 1
n: 10
w: 仓木麻衣
g_tk: 210864166
loginUin: 344319484
hostUin: 0
format: json
inCharset: utf8
outCharset: utf-8
notice: 0
platform: yqq.json
needNewCode: 0'''

headers = dict([line.split(": ",1) for line in headers.split("\n")])
print(headers)