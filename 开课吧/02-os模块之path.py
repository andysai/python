import os

# 返回文件夹的绝对路径
result = os.path.abspath('./文件夹的名字')
print(result)

# 判断是否是文件夹
result = os.path.isdir('./文件夹的名字')
print(result)

# 判断是否是文件
result = os.path.isfile('./文件夹的名字')
print(result)

# 将文件名进行拆分
result = os.path.splitext('批量修改文件名.ipynb')
print(result)

# 判断文件/文件夹的路径是否存在
result = os.path.exists('E:\study\python\开课吧\文件夹的名字')
print(result)

# 文件/文件夹创建的时间 返回的是秒数
result = os.path.getctime('E:\study\python\开课吧\文件夹的名字')
print(result) # 1970-01-01 00:00:00

# 拓展 改变时间戳
import time
timearr = time.localtime(result)
mytime = time.strftime('%Y-%m-%d %H:%M:%S',timearr)
print(mytime)