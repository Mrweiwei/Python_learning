def fib(n):
    '''斐波纳契数列的非递归写法，输出所有小于N的序列'''
    a,b=1,1
    while a<n:
        print(a,end=' ')
        a,b=b,a+b
    print()

fib(1000)

def fibd(n):
    '''斐波纳契数列的递归写法，输出最后的第n个的值'''
    if n<3:
        return 1
    else:
        return fibd(n-1)+fibd(n-2)


#递归计算N=33以后的值就没结果了(计算缓慢)
fib=fibd(16)
print(fib)


