#_*_ coding:utf-8 _*_
#开发人员：34431
#开发时间：2020-02-15 22:32
#文件名称:房屋分期付款.py
#开发工具：PyCharm

# 房子每平方的价格
ppsm = int(input('请输入每平方的价格:'))
# 房子大小
Housing_size = int(input('请输入房屋大小m2:'))
# 房屋总价
all_price = ppsm * Housing_size
# 首付价格
shoufu = all_price * 0.5
# 剩余分期金额
fenqi_fee = all_price - shoufu
# 每年支付价格
fenqi_year = fenqi_fee / 10
# 每月支付价格
fenqi_month = fenqi_year / 12

print('每平方价格:' + str(ppsm) + '\n' + '房屋大小:' + str(Housing_size) + '\n' + '房屋总价:'
      + str(all_price) + '\n' + '首付价格:' + str(shoufu) + '\n' + '剩余分期金额:'
      + str(fenqi_fee) + '\n' + '分期年限总价:' + str(fenqi_year) + '\n' + '分期每月价格:'
      + str(fenqi_month))