#使用pickle模块
'''序列化，简单的说就是把内存中的数据在不丢失的其类型的信息的情况下转成对象的二进制形式
的过程，对象序列化后的形式经过正确的反序列化过程应该能够准确无误地恢复为原来的对象。
    Python中常见的序列化模块有struct、pickle、json、marshal和shelve'''

import pickle
'''pickle是较为常用并且速度非常快的二进制文件序列化模块'''

f=open('sample_pickle.dat','wb')
n=7
i=13000000
a=99.056
s='中国人民 123bc'
lst=[[1,2,3],[4,5,6],[7,8,9]]
tu=(-5,20,8)
coll={4,5,6}
dic={'a':'apple','b':'n=banana','g':'grape','o':'orange'}
try:
    pickle.dump(n,f)
    pickle.dump(i,f)
    pickle.dump(a,f)
    pickle.dump(s,f)
    pickle.dump(lst,f)
    pickle.dump(tu,f)
    pickle.dump(coll,f)
    pickle.dump(dic,f)
except:
    print('写文件异常')
finally:
    f.close()


