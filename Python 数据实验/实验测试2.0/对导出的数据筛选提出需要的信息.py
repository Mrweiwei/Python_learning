import openpyxl
from openpyxl import load_workbook
import pandas as pd

#筛选获得的数据进行读取
wb=load_workbook("Mysql数据库中导出的数据.xlsx")
ws=wb.worksheets[0]

#商品名称
Shopping_name= []
for i in ws["C"]:
  Shopping_name.append(i.value)
#print(list_sheet1_column_C )

#商品数量
Shopping_num=[]
for _ in ws["D"]:
    Shopping_num.append(_.value)
#print(Shopping_num)      

#商品金额
Shopping_money=[]
for _ in ws["E"]:
    Shopping_money.append(_.value)
#print(Shopping_money)

#工作表2
ws1=wb.worksheets[1]
#print(ws1["A"][0].value)
#ws1["A"+str(1)].value=Shopping_name[5]
#存入需要的数据
for i in range(1,len(Shopping_name)+1):
    ws1["A"+str(i)].value=Shopping_name[i-1]
ws1.column_dimensions['A'].width = 70.0

for i in range(1,len(Shopping_money)+1):
    ws1["B"+str(i)].value=Shopping_money[i-1]
ws1.column_dimensions['B'].width = 10.0

for i in range(1,len(Shopping_num)+1):
    ws1["C"+str(i)].value=Shopping_num[i-1]
ws1.column_dimensions['C'].width = 10.0

#合并重复的数据
wb=pd.groupby(["商品名"]).sum

#追加一列统计总金额
ws1["D1"]="总金额"
for row in range(2,len(Shopping_num)+1):
    row=str(row)
    ws1["D"+row]='=C{0}*B{0}'.format(row)
wb.save("Mysql数据库中导出的数据.xlsx")
    
    



    
    
















    
