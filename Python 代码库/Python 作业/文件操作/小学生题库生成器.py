#小学生题库生成器（本例主要演示使用扩展库docx创建Word文档，GUI标准库tkinter）

import random
import os
import tkinter
import tkinter.ttk
from docx import Document
'''python3移除了exceptions模块，所以只安装docx会出现ModuleNotFoundError: No module named 'exceptions'的错误。只需要安装python-docx就可以啦！pip instal python-docx或者直接在pycharm的settings里面添加都可以。
'''
columnsNumber=4

def main(rowsNumber=20,grade=4):
    if grade<3:
        operators='+-'
        biggest=20
    elif grade<=4:
        operators='+-*/'
        biggest=100
    elif grade==5:
        operators='+-*/('
        biggest=100
         
    document=Document()
    #创建表格
    table=document.add_table(rows=rowsNumber,cols=columnsNumber)
    #遍历每个单元格
    for row in range(rowsNumber):
        for col in range(columnsNumber):
            first=random.randint(1,biggest)
            second=random.randint(1,biggest)
            operator=random.choice(operators)
            if operator!='(':
                if operator=='-':
                    #如果是减法口算题，确保结果为正数
                    if first<second:
                        first,secon=second,first
                r=str(first).ljust(2,'')+''+operator+str(second).ljust(2,'')+'='
            else:
                #生成带括号的口算题，需要3个数字和2个运算符
                third=random.randint(1,100)
                while True:
                    o1=random.choice(operators)
                    o2=random.choice(operators)
                    if o1!='(' and o2!='(':
                        break
            rr=random.randint(1,100)
            if rr>50:
                if o2=='-':
                    if second<third:
                        second,third=third,second
                r=str(first).ljust(2,'')+o1+'('\
                    +str(second).ljust(2,'')+o2+str(third).ljust(2,'')+')='
            else:
                if o1=='-':
                    if first<second:
                        first,second=second,first
                r='('+str(first).ljust(2,'')+o1\
                    +str(second).ljust(2,'')+')'\
                    +o2+str(third).ljust(2,'')+'='
        #获取指定单元格并写入口算题
        cell=table.cell(row,col)
        cell.text=r
    document.save('口算.docx')
    os.startfile('口算.docx')


if __name__=='__main__':
    app=tkinter.Tk()#k小写
    app.title('口算-------魏巍')
    app["width"]=300
    app["height"]=150
    labelNumber=tkinter.Label(app,text='Number:',justify=tkinter.RIGHT,width=50)
    labelNumber.place(x=10,y=40,width=50,height=20)
    comboNumber=tkinter.ttk.Combobox(app,values=(100,200,300,400,500),width=50)
    comboNumber.place(x=70,y=40,width=50,height=20)

    labelGrade=tkinter.Label(app,text='Grade:',justify=tkinter.RIGHT,width=50)
    labelGrade.place(x=130,y=40,width=50,height=20)
    comboGrade=tkinter.ttk.Combobox(app,values=(1,2,3,4,5),width=50)
    comboGrade.place(x=200,y=40,width=50,height=20)

    def generate():
        number=int(comboNumber.get())
        grade=int(comboGrade.get())
        main(number,grade)
    buttonGenerate=tkinter.Button(app,text='GO',width=40,command=generate)
    buttonGenerate.place(x=130,y=90,width=40,height=30)

    app.mainloop()






















    
    
                        



























                        
                                        
























    
