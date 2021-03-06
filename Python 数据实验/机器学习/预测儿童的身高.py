'''利用线性回归模型LinearRgression预测儿童身高'''

import copy
import numpy as np
from sklearn import linear_model

#训练数据，每一行表示一个样本，包含的信息分别为：儿童年龄，性别(0女1男)，父亲、母亲、祖父、祖母、外祖父、外祖母身高
x=np.array([[1,0,180,165,175,165,170,165],
            [3,0,180,165,175,165,173,165],
            [4,0,180,165,175,165,170,165],
            [6,0,180,165,175,165,170,165],
            [8,1,180,165,175,167,170,165],
            [10,0,180,166,175,165,170,165],
            [11,0,180,165,175,165,170,165],
            [12,0,180,165,175,165,170,165],
            [13,1,180,165,175,165,170,165],
            [14,0,180,165,175,165,170,165],
            [17,0,170,165,175,165,170,165]])

#儿童身高,单位:cm
y=np.array([60,90,100,110,130,140,150,164,160,163,168])
#创建线性回归模型
lr=linear_model.LinearRegression()

#根据已知数据拟合最佳直线
lr.fit(x,y)
#待测的未知数据，其中每个分量的含义和训练数据相同
xs=np.array([[10,0,180,165,175,165,170,165],
             [17,1,173,153,175,161,170,161],
             [34,0,170,165,170,165,170,165]])

for item in xs:
            #为不改变原始数据，进行深复制，并假设超过18岁以后就不在长高了
            #对于18岁以后的年龄，返回18岁时的身高
            item1=copy.deepcopy(item)
            if item1[0] >18:
                item1[0]=18
            print(item,':',lr.predict(item1.reshape(1,-1)))


























