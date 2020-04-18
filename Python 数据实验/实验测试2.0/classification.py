#使用百度云智能API接口实现精准分词的功能
from aip import AipNlp
#导入未分类的邮箱库
from Mail_data import Mail_list

APP_ID='19122578'
API_KEY='e8d071gY19ns8XyOxh5GrSry'
SECRET_KEY='LXmHT90WXhiGvexhsGd9FLabt6PSGtDf'
client=AipNlp(APP_ID,API_KEY,SECRET_KEY)

#Mail_list:邮件列表  stop_word:停词库
stop_word={}.fromkeys(['狗','虫子','猫','猪'])
#print(Mail_list[2]["theme"])

def classify(lst,j):
    '''分类函数'''
    for word in lst:
        if word not in stop_word:
            Mail_list[j]["category_id"]=0
        else:
            Mail_list[j]["category_id"]=1
        
for j in range(len(Mail_list)):
    text=Mail_list[j]["theme"]
    lst=client.dnnlm(text)["items"]
    done=[]
    for i in range(len(lst)):
        done.append(str(lst[i]["word"]))
        #去掉分词后的句号
        if '，' in done:
            done.remove('，')
    classify(done,j)

#分完词后存入excel表格中
import openpyxl
from openpyxl import Workbook


#创件一个Excel文件
workbook=Workbook()
#创建一个工作表
worksheet=workbook.worksheets[0]
#逐行写入表格
for row in Mail_list:
    line=[]
    line.append(row[0])
    line.append(row[1])
    worksheet.append(line)
#保存出表  
workbook.save("email_data_classified.xlsx")












    

