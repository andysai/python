# 数据探索性分析
import pandas as pd
sale_data = 'sale_data.xls'   # 这里可以写相对路径
data = pd.read_excel(sale_data, index_col='日期')
# print(data)

data1 = data.describe()
# print(data1)

import matplotlib.pyplot as plt

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
# 显示正负号
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(5,10))
p = data.boxplot(return_type='dict')
# 显示异常点的值
x = p['fliers'][0].get_xdata()
y = p['fliers'][0].get_ydata()
y.sort()

for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy= (x[i],y[i]), xytext=(x[i] + 0.05 - 0.8/(y[i]-y[i-1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i],y[i]), xytext=(x[i]+0.08,y[i]))
plt.show()

# 数据特征分析中的贡献度分析 帕累托分析 二八原则
dish_profit = 'dish_profit.xls'
data = pd.read_excel(dish_profit, index_col='菜品名')
data = data['盈利'].copy()
plt.figure(figsize=(15, 6))
data.plot(kind='bar')
plt.ylabel("盈利(元)")

p = 1.0 * data.cumsum() / data.sum()
p.plot(color='r', secondary_y=True, style='-o', linewidth=2)

plt.annotate(format(p[6], '.4f'),
             xy=(6, p[6]),
             xytext=(6 * 0.9, p[6] * 0.9),
             arrowprops=dict(arrowstyle='->',
                             connectionstyle='arc3,rad=.2')

             )

plt.ylabel("盈利的比例")
plt.show()

# 对缺失值的处理
# 拉格朗日差值
from scipy.interpolate import lagrange
#  定义两个文件，输入文件和结果输出文件
inputfile = 'sale_data.xls'
outputfile = 'tem_sales.xlsx'

# 读取输入文件数据
data = pd.read_excel(inputfile)

# 定义异常数据的含义比如说，销量小于400 或销量大于5000，我们认为他是异常异常数据,就把他变为控制
data['销量'][(data['销量'] < 400) | (data['销量'] > 5000)] = None

# 自定义一个列向量插值的函数
# s是列向量， n是被插值的位置，k是取前后的数据的个数
def insert_column_data(s, n, k=5):
    # 取数
    y = s[list(range(n-k)) + list(range(n+1, n+1+k))]
    # 提出空值
    y = y[y.notnull()]
    return lagrange(y.index, list(y))(n)

# 我们现在来逐个依次的判断是否需要插值
for i in data.columns:
    for j in range(len(data)):
        if (data[i].isnull())[j]: # 如果为空就插值
            data[i][j] = insert_column_data(data[i], j)

# 将输出的结果，写入到文件中
data.to_excel(outputfile)