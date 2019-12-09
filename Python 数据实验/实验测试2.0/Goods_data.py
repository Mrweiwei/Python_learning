import openpyxl
from openpyxl import load_workbook

#读取数据
wb=load_workbook("商品数据.xlsx")
ws=wb.worksheets[0]

#定义一个商品列表Goods_list，这是一个字典列表，列表中的每个元素都是一个字典
Goods_list=[]

'''a={"title":"asd"}
Goods_list.append(a)
print(Goods_list[0]["title"])'''

#商品名称
Shopping_name= []
for i in ws["A"]:
  Shopping_name.append(i.value)
#print(Shopping_name[0])
#商品金额
Shopping_money=[]
for _ in ws["C"]:
    Shopping_money.append(_.value)
#print(Shopping_money)

#详情地址
Shopping_url=[]
for _ in ws["B"]:
    Shopping_url.append(_.value)
#print(Shopping_url)

for m in range(len(Shopping_name)):
    a={}
    a["title"]=Shopping_name[m]
    a["price"]=Shopping_money[m]
    a["url"]=Shopping_url[m]
    Goods_list.append(a)

#print(Goods_list[0]["title"])
    










    
        
        

    
