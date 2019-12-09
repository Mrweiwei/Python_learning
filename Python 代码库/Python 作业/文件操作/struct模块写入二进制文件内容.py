#使用struct模块
'''struct也是比较常用的对象序列化和二进制文件读写模块'''
import struct

n=1300000
x=96.45
b=True
s='al@ 中国'
sn=struct.pack('if?',n,x,b)
f=open('sample_struct.dat','wb')
f.write(sn)
f.write(s.encode('utf-8'))
f.close()
