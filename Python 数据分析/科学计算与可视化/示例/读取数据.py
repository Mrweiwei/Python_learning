#键盘品牌分析
#读取数据

import os
import pandas as pd

#数据统计函数
def get_list_num(l):
    name=list(set(l))#名字
    value=[]#次数
    for item in name:
        value.append(l.count(item))
    return name,value

#获取当前文件父目录路径
father_path=os.getcwd()
#原始数据文件路径
rpath_csv=father_path+r'/rich_list.csv'
#读取数据
csv_read=pd.read_csv(rpath_csv)
#print(csv_read)

#品牌分析

manufacturer=list(csv_read[3])
statistical=get_list_num(manufacturer)

#可视化
from cutecharts.charts import Bar

def bar_base()->Bar:
    chart=Bar("3-7月键盘品牌")
    chart.set_options(labels=statistical[0],x_label="品牌名",y_label="出现次数")
    chart.add_series("品牌频数比较",statistical[1])
    return chart

bar_base().render("3-7月键盘品牌柱状图.html")

#数据处理

#获取每个品牌对应的排名总和
rank_list=[]
for i in statistical[0]:
    table=csv_read.loc[csv_read["C1"]==i]
    rank_list.append(sum(table["A1"])/5)#排名计算总和都除五

#可视化分析
from cutecharts.charts import Line

def line_base()->Line:
    chart=Line("3-7月键盘品牌")
    chart.set_options(labels=statistical[0],x_label="品牌名",y_label="总数")
    chart.add_series("品牌频数",statistical[1])
    chart.add_series("品牌排名",rank_list)
    return chart

line_base().render()

index_list=[]
#选取三个较热门的产品
model=["MX8.0","K70","雷柏V500"]
for i in model:
    print(i)
    table=csv_read.loc[csv_read["B1"]==i]
    print(table)#显示查询数据











    
























