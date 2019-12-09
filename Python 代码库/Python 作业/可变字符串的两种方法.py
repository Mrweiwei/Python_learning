#在python中，字符串属于不可变对象，不支持原地修改，如果需要修改其中的值，只能重新
#创建一个新的字符串对象。然而，如果确实需要一个支持原地修改的Unicode数据对象，可以
#使用io.StringIO()对象或array模块

import io
s='Hello,World'
sio=io.StringIO(s)
sio.getvalue()
sio.seek(6)
sio.write("there!")
print(sio.getvalue())

import array
a=array.array('u',s)
print(a)
a[0]='y'
print(a)
print(a.tounicode())
