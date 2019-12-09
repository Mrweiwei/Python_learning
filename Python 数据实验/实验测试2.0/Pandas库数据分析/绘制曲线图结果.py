#结合matplotlib绘图

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#绘制双曲线图
df=pd.DataFrame(np.random.randn(1000,2),columns=['B','C']).cumsum()
df['A']=pd.Series(list(range(len(df))))
#plt.figure()
df.plot(x='A')


#绘制纵向柱状图
df1=pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
df1.plot(kind='bar')


#绘制水平柱状图
df1.plot(kind='barh',stacked=True)

plt.show()

'''文件读写方法:
                写Excel:df.to_excel('文件路径',sheet_name='')
                读取Excel:df1=pd.read_excel('文件路径','sheet_name',index_col=None,na_values=['NA'])
                将数据保存为csv文件:df1.to_csv('文件路径')
                读取csv文件中的数据：df2=pd.read_csv('文件路径')
                '''
