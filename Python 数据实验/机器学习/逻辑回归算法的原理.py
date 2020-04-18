'''演示逻辑回归算法的原理'''

import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

#构造测试数据
X=np.array([[i] for i in range(30)])
y=np.array([0]*15+[1]*15)

#人为修改部分样本的值
y[np.random.randint(0,15,3)]=1
y[np.random.randint(15,30,4)]=0
print(y[:15])
print(y[15:])

#根据原始数据绘制散点图
plt.scatter(X,y)

#创建并训练逻辑回归模型
reg=LogisticRegression()
reg.fit(X,y)

#对未知数据进行预测
print(reg.predict([[5],[19]]))
#未知数据属于某个类别的概率
print(reg.predict_proba([[5],[19]]))

#对原始观察点进行预测
yy=reg.predict(X)
#根据预测结果绘制折线图
plt.plot(X,yy)

plt.show()




