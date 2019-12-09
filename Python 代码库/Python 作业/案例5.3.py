#编写函数，接收字符串参数，返回一个元组，其中第一个元素为大写字母个数，第二个元素为小写字母个数

def demo(s):
    result=[0,0]
    for ch in s:
        if 'a'<=ch<='z':
            result[1]+=1
        elif 'A'<=ch<='Z':
            result[0]+=1
    return tuple(result)


print(demo('aaaaabbbbbc'))
