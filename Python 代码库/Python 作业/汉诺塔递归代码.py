#汉诺塔将A塔上所有的圆盘放在C塔上并写出每步的过程
count=0
def hanio(n,a,b,c):
    global count
    if n==1:
        count+=1
        print('移动第',count,'次',a,'-->',c)
    else:
        hanio(n-1,a,c,b)
        hanio(1,a,b,c)
        hanio(n-1,b,a,c)
        
while True:
    num=input('请用户输入任意个圆盘数：')
    hanio(eval(num),'塔A','塔B','塔C')
    print('一共移动了',count,'次')
    s=input('是否继续玩？(y/n)')
    if s=='n':
        break

