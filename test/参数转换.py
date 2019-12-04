# 请求参数转换
headers = '''i: like
from: AUTO
to: AUTO
smartresult: dict
client: fanyideskweb
salt: 15754627910321
sign: e27312568eabdeddd88c6e4882c73b0b
ts: 1575462791032
bv: ec579abcd509567b8d56407a80835950
doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_REALTlME'''

headers = dict([line.split(": ",1) for line in headers.split("\n")])
print(headers)