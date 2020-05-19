# 导入os模块
import os

# 获取当前目录
print(os.getcwd())

# 获取当前操作系统的类型 posix为linux、unix系统,nt为windows系统
print(os.name)

# 创建一个文件夹 ./代表当前目录
print(os.mkdir('./文件夹的名字'))