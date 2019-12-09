'''Pandas(Python Data Analysis Library)基于Numpy构建，让基于
Numpy的应用更简单，被广泛应用更简单，被广泛应用于金融行业，流行
的数据分析工具'''
'''Pandas主要有两种数据结构：
        系列（Series）:是能够保存任何类型的数据（整数，字符串，
浮点数，Python对象等）的一维标记数组。轴标签统称为索引。
        数据帧(DataFrame)是二维数据结构，即数据以行和列的表格
方式排列。数据帧的特点：
        潜在的列是不同的类型
        大小可变
        标记轴（行和列）
        可以对行和列执行算术运算'''

import pandas as pd

#创建Series

obj=pd.Series([1,3,24,23,8],index=['a','b','c','d','e'])  #index值可以自定义
print(obj)
print(obj.values)
print(obj.index)
print(obj[3])

#DataFrame
data={'name':['calvin','kobe','michale','durant','james'],'age':[29,40,56,30,34],'height':[1.70,1.98,1.98,2.06,2.03]} #从字典创建DataFrame
data2=[['a',1],['b',2],['c',3]]#从列表创建DataFrame
data3={'one':pd.Series([1,2,3],index=['a','b','c']),
'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}#从
#系列的字典来创建DataFrame
dd=pd.DataFrame(data3)
df=pd.DataFrame(data2,columns=['name','age'])#加入列标签
dd['three']=pd.Series([10,20,30],index=['a','b','c'])#增加列
del dd['one']#删除列
print(df)
print (dd) 
print(dd['two']) #列选择
print(dd.loc['b'])  #行选择(标签选择)
print(dd.iloc[1]) #行选择(按整数位置选择)
print(dd[0:2]) #行切片


























