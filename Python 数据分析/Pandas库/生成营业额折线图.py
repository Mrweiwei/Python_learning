#开始分析
import pandas as pd
import matplotlib.pyplot as plt

#读取数据，丢失缺失值
df=pd.read_csv("data.csv",encoding="cp936")
df=df.dropna()

#生成营业额折线图
plt.figure()
df.plot(x=df['日期'].values)
plt.savefig('折线图.jpg')
