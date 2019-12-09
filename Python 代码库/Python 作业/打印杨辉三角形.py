#编写函数，接收一个整数t作为参数，打印杨辉三角形的前t行

def Yanghui(t):
    '''打印杨辉三角形的前t行'''
    print([1])
    print([1,1])
    line=[1,1]
    for i in range(2,t):
        r=[]
        for j in range(0,len(line)-1):
            r.append(line[j]+line[j+1])
        line=[1]+r+[1]
        print(line)


Yanghui(10)
