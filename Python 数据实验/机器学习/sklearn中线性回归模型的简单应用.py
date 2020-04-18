from  sklearn import linear_model #导入线性模型快

regression=linear_model.LinearRegression()  #创建线性回归模型

X=[[3],[8]] #观察值的x坐标
y=[1,2]     #观察值的y坐标
regression.fit(X,y) #拟合
#LinearRegression(copy_X=True,fit_intercept=True,n_jobs=1,normalize=False)

print(regression.intercept_) #截距，以下画线结束
print(regression.coef_) #斜率，回归系数反映了x对y影响的大小，以下画线结束，表示模型自身的属性，区别于用户设置的参数

print(regression.predict([[6]]))  #对未知点进行预测，结果为数组

print(regression.score([[6],[7],[8],[9],[10]],[1.6,1.8,1.99,2.2,2.401]))  #对模型进行评分，结果越大越好
