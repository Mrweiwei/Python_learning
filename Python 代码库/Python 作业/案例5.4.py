#编写函数，接收包含20个整数的列表lst和一个整数k作为参数，返回新列表。处理规则为：将列表lst中小标k之前
#的元素逆序，小标k之后的元素逆序，然后将整个列表lst中的所有元素逆序


def demo(lst,k):
    x=lst[:k]
    x.reverse()
    y=lst[k:]
    y.reverse()
    r=x+y
    r.reverse()
    return r


lst=list(range(1,21))
print(lst)
print(demo(lst,5))
