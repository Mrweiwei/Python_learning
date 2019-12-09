from math import pi as PI #as …… ：取个别名

def CircleArea(r):
    '''编写计算圆的面积的函数'''
    if (isinstance(r,int) or isinstance(r,float))and r>0:#确保接收的参数为大于零的数字
        return PI*r**2
    else:
        return('请您输入正确的半径')


print(CircleArea(3))
