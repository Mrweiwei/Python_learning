import pandas as pd

data=pd.read_excel('data.xlsx',sep=',',encoding='gbk')
x=data[['平均消费周期（天）','平均每次消费金额']].values#.as_matrix()将被替换，用.values替换
#导入聚类分析工具KMeans
from sklearn.cluster import KMeans
#传入要分类的数目
kms=KMeans(n_clusters=3)
y=kms.fit_predict(x)
print(y)

'''pandas中既可以用read_csv和to_csv对csv文件进行读写
又可以对excel文件用read_excel和to_excel进行读写'''
