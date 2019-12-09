#使用struct模块读取二进制内容

import struct

f=open('sample_struct.dat','rb')
sn=f.read(9)
tu=struct.unpack('if?',sn)
print(tu)
n,x,b1=tu
print('n=',n,'x=',x,'b1=',b1)
s=f.read(9)
s=s.decode('utf-8','ignore')      
print('s=',s)
