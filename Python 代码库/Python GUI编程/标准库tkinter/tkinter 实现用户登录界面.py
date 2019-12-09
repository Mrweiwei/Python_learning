'''用户登录界面：
                用户登录界面几乎无处不在，用户输入用户名、账号和密码后，系统进行验证，通过验证才可以进行后续的操作
                。一般而言，用户密码都是经过安全哈希算法加密之后存储到数据库中的，并不直接保存明文
'''
#tkinter实现用户登录界面（使用tkinter创建应用程序窗口，以及文本框、按钮和简单消息框等组件用法。）

import tkinter
import tkinter.messagebox

def login():               #登录按钮事件处理函数
    name=entryName.get()   #获取用户名
    pwd=entryPwd.get()     #获取密码
    if name=='weiwei' and pwd=='peter':
        tkinter.messagebox.showinfo(title='Python tkinter',message="恭喜您成功登录系统！")
    else:
        tkinter.messagebox.showerror('Python tkinter',message="您输入的用户名或者密码有误！")

def cancel():
    varName.set('')     #清空用户输入的用户名和密码
    varPwd.set('')

root=tkinter.Tk()
varName=tkinter.StringVar(value='')
varPwd=tkinter.StringVar(value='')
labelName=tkinter.Label(root,text='用户名:',
                        justify=tkinter.RIGHT,width=80
                        )#创建标签
labelName.place(x=10,y=5,width=80,height=20)#将标签放到窗口上
entryName=tkinter.Entry(root,width=80,
                        textvariable=varName)#创建文本框同时设置关联的变量
entryName.place(x=100,y=5,width=80,height=20)
labelPwd=tkinter.Label(root,text='密码:',justify=tkinter.RIGHT,width=80)
labelPwd.place(x=10,y=30,width=80,height=20)
entryPwd=tkinter.Entry(root,show='*',
                       width=80,textvariable=varPwd)#创建密码文本框
entryPwd.place(x=100,y=30,width=80,height=20)

buttonOk=tkinter.Button(root,text='登录',
                            command=login)#创建按钮组件同时设置按钮事件处理函数
buttonOk.place(x=30,y=70,width=50,height=20)
buttonCancel=tkinter.Button(root,text='取消',
                            command=cancel)
buttonCancel.place(x=90,y=70,width=50,height=20)

root.mainloop()     #启动消息循环

























