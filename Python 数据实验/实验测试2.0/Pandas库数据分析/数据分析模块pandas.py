#数据分析模块pandas
'''pandas(Python Data Analysis Library)是基于NumP的数据分析模块，提供了大量的标准数据模型和高效操作大型数据集
所需要的工具，可以说pandas是使得Python能够成为高效且强大的数据分析环境的重要因素之一
   pandas主要提供了3种数据结构: 1.Series,带标签的一位数组
                               2.DataFrame,带标签且大小可变的二维表格结构
                               3.Panel,带标签且大小可变的三维数组'''

import pandas as pd
import numpy as np

#生成一维数组
x=pd.Series([1,3,5,np.nan],index=('a','b','c','d'))#Series里面的默认index值是数字，可以修改
print("利用pd.Series()生成一维数组:")
print(x)

#生成二维数组
dates_Day=pd.date_range(start='20190101',end='20191231',freq='D')#间隔为天,间隔属性为freq，'H','D','W','M'.
print('pd.date_range生成以天数计算的二维数组:')
print(dates_Day)

df=pd.DataFrame(np.random.randint(4,12),index=dates_Day,columns=list('ABCD'))
print(df)

dates_Month=pd.date_range(start='20190101',end='20191231',freq='M')
df=pd.DataFrame([[np.random.randint(1,100) for j in range(4)]for i in range(12)],index=dates_Month,columns=list('ABCD'))
print(df)#4位列随机数

df=pd.DataFrame({
    'A':[np.random.randint(1,100)for j in range(5)],
    'B':pd.date_range(start='20190101',periods=5,freq='D'),
    'C':pd.Series([1,2,3,4,5],index=list(range(5)),dtype='float32'),
    'D':np.array([3]*5,dtype='int32'),
    'E':pd.Categorical(["test","train","test","train","你的太阳"]),
    'F':'love u'
    })
print(df)

#二维数据的查看
print(df.head())  #默认查看前5行
print(df.head(3)) #查看前3行
print(df.tail(2)) #查看最后两行

#查看二维数据的索引、列名和数据
print("索引值为：",df.index)
print("列的名为：",df.columns)
print("数据为：",df.values)

#查看数据的统计信息
print(df.describe()) #平均值、标准差、最小值、最大值等信息

#二维数据的转置
print(df.T)

#排序
print(df.sort_index(axis=0,ascending=False))   #对纵轴元素进行降序排序
print(df.sort_index(axis=1,ascending=True))    #对横轴元素进行升序排序
print(df.sort_values(by='A'))                  #对数据按照A列进行升序排序
print(df.sort_values(by='A',ascending=False))  #降序排序

#数据选择
print(df['A'])   #选择列
print(df[0:2])   #使用切片选择多行
print(df.loc[:,['A','C']])#选择A和C列所有行的数据
print(df.loc[[2,3],['A','D','E']])#同时选定多行多列的数据值
print(df.loc[2,['A','D','E']])    #同时选定1行多列的数据值
print(df.at[2,'A'])               #查询指定行、列位置的数据值
print(df.iloc[0:3,0:4])           #查询前3行、前4列数据
print(df.iloc[[0,2,3],[0,4]])     #查询多行、多列位置的数据值
print(df.iloc[2,2])               #查询指定行、列位置的数据值
print(df[df.A>50])                #按条件查询

#数据的修改与设置
df.iat[0,2]=3
print("修改指定行、列位置的数据值")
print(df)
df.loc[:,'D']=[np.random.randint(50,60)for i in range(5)]
print("修改了D列的所有值")
print(df)
df['C']=-df['C']
print("对指定列数据取反")
print(df)























































