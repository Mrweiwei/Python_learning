import pickle

f=open('sample_pickle.dat','rb')
n=pickle.load(f)          #读出文件的数据个数
i=0
while i<n:
    x=pickle.load(f)
    print(x)
    i+=1
f.close()
