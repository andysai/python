# 销售预测

# 环境说明
# - 项目描述： 投放金额与销售额预测
# - 作者： 贪心学院 出品
# - 基础环境：Python3.7
# - 依赖库：pandas、Matplotlib、sklearn、numpy
# - 输入数据： data.txt
# - 程序输出目标：要对销售额进行预测
# - 模型应用： 线性回归
# - 环境安装基本命令： pip install pandas 或 matplotlib 或 sklearn
# - 应用软件: jupyter notebook  安装方式 pip install jupyter

# 导入库
# 导入数据分析的pandas库
import pandas as pd
# 导入画图库
from matplotlib import pyplot as plt
# 导入模型库   线性回归
from sklearn import linear_model
# 导入算法评价函数  均方误差
from sklearn.metrics import mean_squared_error

# 数据读取
data = pd.read_csv('data.txt')
# print(data)

# 数据预处理
num = int(data.shape[0]*0.7)
x,y = data[['money']],data[['amount']]
x_train,x_test = x[:num],x[num:]
y_train,y_test = y[:num],y[num:]

# 数据探索分析
plt.scatter(x_train,y_train)

# 数据建模
model = linear_model.LinearRegression()
model.fit(x_train,y_train)

# 模型评估
predict_test_y = model.predict(x_test)
print("MSE均方误差是: %.2f" % mean_squared_error(y_test,predict_test_y))

# 预测
import numpy as np
new_x = np.array([[84632]])
pre_y = model.predict(new_x)
print(pre_y)