#统计所有演员参演信息

import openpyxl
from openpyxl import Workbook

def getActors(filename):
    actors=dict()
    wb=openpyxl.load_workbook(filename)
    ws=wb.worksheets[0]
    for index,row in enumerate(ws.rows):
        #绕过第一行的表头
        if index==0:
            continue
        #获取电影名称和演员列表
        filmName,actor=row[0].value,row[2].value.split('，')
        #遍历该电影的所有演员，统计参演电影
        for a in actor:
            actors[a]=actors.get(a,set())|{filmName}
    return actors

actors=getActors('电影导演演员.xlsx')
#排序
actors=sorted(actors.items(),key=lambda x:int(x[0][2:]))
for item in actors:
    print(item)

















