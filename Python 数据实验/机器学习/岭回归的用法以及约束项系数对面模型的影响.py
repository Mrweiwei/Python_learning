'''岭回归的基本原理与sklearn实现
岭回归是一种用于共线性数据（自变量之间存在较强的线性关系）分析的有偏估计回归方法，是改良的最小二乘估计法，通过放弃
最小二乘法的无偏性，以损失部分信息、降低精度为代价从而获得更符合实际、更可靠的回归系数，对病态数据（这样的数据中某
个元素的微小变动会导致计算结果误差很大）的拟合效果比最小二乘法好。岭回归通过在代价函数后面加上一个对参数的约束项（
回归系数向量的l2范数与一个常数a的乘积,称作L2正则化）来防止过拟合，即书上151上的公式
'''

from sklearn.linear_model import Ridge
ridgeRegression=Ridge(alpha=10)  #创建岭回归模型

X=[[3],[8]]
y=[1,2]
ridgeRegression.fit(X,y)  #拟合

print(ridgeRegression.predict([[6]]))
