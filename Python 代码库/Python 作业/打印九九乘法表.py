#打印九九乘法表
print('九九乘法表如下：',end='\n')
for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,'\t',end='') #/t 表示制表符
    print()
