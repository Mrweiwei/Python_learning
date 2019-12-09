#编写函数，接收整数参数t，返回斐波纳契数列大于t的第一个数：

def demo(t):
    a,b=1,1
    while b<t:
        a,b=b,a+b
    return b

print(demo(50))
