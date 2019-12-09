#编写函数，接收任意多个实数，返回一个元组，其中第一个元素为所有参数的平均值，其他元素为所有参数中大于平均值的实数

def demo(*para):
    avg=sum(para)/len(para)  #注意Python2.x与3.x对除法运算符"/"的解释不同
    g=[i for i in para if i >avg]
    return (avg,)+tuple(g)

print(demo(1,2,3,4))
