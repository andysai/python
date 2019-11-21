# -*- coding: UTF-8 -*-
# 导入email相应的模块
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 发信方的信息：发信邮箱，QQ邮箱授权码或油箱密码
from_addr = 'czl@casc.ac.cn'
password = 'idc888888'

# 接收方的信息：接收邮箱
to_addr = ['344319484@qq.com']

# 发信服务器
server_smtp = 'mail.casc.ac.cn'

# 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
text = """你好：
    这是一个测试文件
"""

msg = MIMEText(text,'plain','utf-8')

# 构建得邮件主题、发件人、收件人信息
msg['From'] = Header(from_addr)
msg['To'] = Header(",".join(to_addr))
msg['Subject'] = Header('Subject Test')

# 开启发信服务，这里使用的是加密传输
server = smtplib.SMTP(server_smtp)
server.starttls()
server.connect(server_smtp,25)

# 登录发信邮箱
server.login(from_addr,password)

# 发送邮件
server.sendmail(from_addr,to_addr,msg.as_string())

# 关闭服务器
server.quit()