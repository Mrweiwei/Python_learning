from random import choices
from collections import Counter
from math import log2
import pandas as pd


#设置输出结果列对齐
pd.set_option('display.unicode.ambiguous_as_wide',True)
pd.set_option('display.unicode.east_asian_width',True)

df=pd.DataFrame({
    '婚否':choices(('是','否'),k=20),
    '工作否':choices(('是','否'),k=20),
    '有车否':choices(('是','否'),k=20),
    '收入水平':choices(('是','否'),k=20),
    '是否有贷款':choices(('是','否'),k=20),
    '结果':choices(('是','否'),k=20)
    })
print('======原始数据：',df,sep='\n')
total_length=len(df)  #原始数据总数量

def get_entropy(values):
    '''计算一组数据的熵'''
    length=len(values)
    #Counter用于统计一组数据中每个数值的出现次数
    return -sum(map(lambda num:num/length*log2(num/length),
                    Counter(values).values()))
#计算原始数据的熵
origin_entropy=get_entropy(df.结果.values)
print('=======原始数据的熵：',origin_entropy,sep='\n')
new_entropy=[] #存放使用每个列/特征进行分类后的信息熵
for column in df.columns[:-1]: #最后一列是分类结果，不用做分类特征
    unique_features=set(df[column].values)#该列所有唯一值
    every_entropy=0 #存放使用该特征分类时每个子类的熵之和
    for feature in unique_features: #遍历每个唯一值，
        values=df[df[column]==feature].结果.values #获取数据，计算该类的熵
        every_entropy+=len(values)/total_length*get_entropy(values)
    new_entropy.append((column,every_entropy))
print('======每个特征的信息增益：',*new_entropy,sep='\n')
best_feature=min(new_entropy,key=lambda item:item[1])[0]
print('=====最佳分类特征：',best_feature,sep='\n')
print('=====使用最佳特征进行分类：')
for value in set(df[best_feature].values):
    print(df[df[best_feature]==value])
























