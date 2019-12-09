#简单的文本编辑器
'''下面的案例通过设计一个文本编辑器演示了菜单、文本框、文件对话框等组件的用法，实现了打开文件、保存文件、另存文件
以及文本的复制、剪切、粘贴和查找功能'''

import tkinter
import tkinter.filedialog
import tkinter.colorchooser
import tkinter.messagebox
import tkinter.scrolledtext

#创建应用程序窗口
app=tkinter.Tk()
app.title('我的文本编辑器----作者:魏巍')
app['width']=800
app['height']=600

textChanged=tkinter.IntVar(value=0)#标记当前内容是否发生过改变，是否需要保存。0:没改过。1：更改过
#当前文件名
filename=''

#创建菜单
menu=tkinter.Menu(app)
#File菜单
submenu=tkinter.Menu(menu,tearoff=0)#tearoff=0表示该菜单不可以独立；1表示子菜单顶端会有一个虚线

def Open():
    global filename
    #如果内容已改变，先保存
    if textChanged.get():
        yesno=tkinter.messagebox.askyesno(title='是否需要保存?',message="你想要保存吗？")
        if yesno==tkinter.YES:
            Save()
    filename=tkinter.filedialog.askopenfilename(title='打开文件',filetypes=[('Text files','*.txt')])

    if filename:
        #清空内容，0.0是第零行第零列的表示方法,END表示最后一行最后一列
        txtContent.delete(0.0,tkinter.END)
        fp=open(filename,'r')
        txtContent.insert(tkinter.INSERT,''.join(fp.readlines()))
        fp.close()
        #标记为尚未修改
        text.Changed.set(0)
#创建Open菜单并绑定菜单事件处理函数
submenu.add_command(label='打开',command=Open)

def Save():
    global filename
    #如果是第一次保存新建文件，则打开“另存为”窗口
    if not filename:
        SaveAS()
    #如果内容发生改变，保存
    elif textChanged.get():
        fp=open(filename,'w')
        fp.write(txtContent.get(0.0,tkinter.END))
        fp.close()
        text.Changed.set(0)
submenu.add_command(label='保存',command=Save)

def SaveAs():
    global filename
    #打开“另存为”窗口
    newfilename=tkinter.filedialog.asksaveasfilename(title='另存为',initialdir=r'c:\\',initialfile='new.txt')
    #如果指定了文件名，则保存文件
    if newfilename:
        fp=open(newfilename,'w')
        fp.write(textContent.get(0.0,tkinter.END))
        fp.close()
        filename=newfilename
        textChanged.set(0)
submenu.add_command(label='另存为',command=SaveAs)

#添加分割线
submenu.add_separator()

def Close():
    global filename
    Save()
    txtContent.delete(0.0,tkinter.END)
    #置空文件名
    filename=''
submenu.add_command(label='关闭',command=Close)
#将子菜单关联到主菜单上
menu.add_cascade(label='文件',menu=submenu)

#Edit菜单
submenu=tkinter.Menu(menu,tearoff=0)
#撤销最后一次操作
def Undo():
    #启用undo标志
    txtContent['undo']=True
    try:
        txtContent.edit_undo()
    except Exception as e:
        pass
submenu.add_command(label='撤销',command=Undo)

def Redo():
    txtContent['undo']=True
    try:
        txtContent.edit_redo()
    except Exception as e:
        pass
submenu.add_command(label='重写',command=Redo)
submenu.add_separator()

def Copy():
    txtContent.clipboard_clear()
    txtContent.clipboard_append(txtContent.selection_get())
submenu.add_command(label='复制',command=Copy)

def Cut():
    Copy()
    #删除所选内容
    txtContent.delete(tkinter.SEL_FIRST,tkinter.SEL_LAST)
submenu.add_command(label='剪切',command=Cut)


def Paste():
    #如果没有选中内容，则直接粘贴到鼠标位置
    #如果有所选内容，则先删除在粘贴
    try:
        txtContent.insert(tkinter.SEL_FIRST,txtContent.clipboard_get())
        txtContent.delete(tkinter.SRL_FIRST,tkinter.SEL_LAST)
        #如果粘贴成功就结束本函数，以免异常处理结构执行完成之后再次粘贴
        return
    except Exception as e:
        pass
    txtContent.insert(tkinter.INSERT,txtContent.clipboard_get())
submenu.add_command(label='粘贴',command=Paste)
submenu.add_separator()


def Search():
    #获取要查找的内容
    textToSearch=tkinter.simpledialog.askstring(title='搜索',prompt='你要搜索什么？')
    start=txtContent.search(textToSearch,0.0,tkinter.END)
    if start:
        tkinter.messagebox.showinfo(title='查询',message='ok')
submenu.add_command(label='搜索',command=Search)
menu.add_cascade(label='编辑',menu=submenu)

#Help菜单
submenu=tkinter.Menu(menu,tearoff=0)
def About():
    tkinter.messagebox.showinfo(title='关于',message='作者:魏巍')
submenu.add_command(label='帮助',command=About)
menu.add_cascade(label='帮助',menu=submenu)
#创建的菜单关联到应用程序窗口
app.config(menu=menu)

#创建文本编辑组件，并且自动适应窗口大小
txtContent=tkinter.scrolledtext.ScrolledText(app,wrap=tkinter.WORD)
txtContent.pack(fill=tkinter.BOTH,expand=tkinter.YES)
def KeyPress(event):
    textChanged.set(1)
txtContent.bind('<KeyPress>',KeyPress)

app.mainloop()























    


























        








































































































    
        



























        






















