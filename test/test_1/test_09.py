import smtplib
from email.mime.text import MIMEText

from_addr = '429448383@qq.com'
password = 'aoginbolncggcahj'
to_addr = '429448383@qq.com'
smtp_server = 'qq.smtp.com'
msg = MIMEText('send by python','plain','utf-8')
server = smtplib.SMTP_SSL(smtp_server)
server.connect(smtp_server,465)
server.login(from_addr,to_addr)
server.sendmail(from_addr,to_addr,msg.as_string())
server.quit()
