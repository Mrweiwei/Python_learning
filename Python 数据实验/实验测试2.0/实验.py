#import Goods_data
import random
#from Mail_data import Mail_list
#from aip import AipNlp
#print(Goods_data.Goods_list[300000])
#for i in range(10):
#print(Goods_data.外卖[i]["title"])
#print(Mail_list[1]["theme"])



'''import jieba

seg_list = jieba.cut("肯德基(新一城店) 地址:朝阳区阜荣街10号新一城大厦沃尔玛1楼 ", cut_all=False)

print(", ".join(seg_list))'''

a=[{'title':'#asd'},
   {'title':'*sf'},
   {'title':'正常'}]


for i in range(len(a)):
    if '#' in a[i]["title"] or '*' in a[i]["title"]:
        a[i]['c']=0
    else:
        a[i]['c']=2
print(a)




        
