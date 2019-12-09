#案例精选(两种注释的方法：1.#代表当前行注释。2."""  """三队引号代表块注释)
#1.计算1+2+3+…+100
#s=0
#for i in range(1,101):
#    s+=i
#print('计算的结果是',s)
#直接使用内置函数实现的方法
#print('计算的结果是',sum(range(1,101)))

#2.输出用户输入的列表和截取范围的数字后得出的子集合
"""lst=eval(input('请用户输入一个列表'))
rng=input('请输入两个范围数字以空格隔开')
num=[]
num.append(int(rng[0]))
num.append(int(rng[2]))
num.sort()
print('您截取的子集合是：',lst[num[0]:num[1]+1])"""

#3.Python版的快速排序算法
"""from random import randint    #引入random模块的dandint类

def quickSort(lst,reverse=False):
    if len(lst)<=1:
        return lst
    #默认使用最后一个元素作为枢点
    pivot=lst.pop()
    first,second=[],[]
    #默认使用升序排序
    exp='x<=pivot'
    #reverse=True表示降序排序
    if reverse==True:
        exp='x>=pivot'
    for x in lst:
        first.append(x) if eval(exp) else second.append(x)
    #递归调用
    return quickSort(first,reverse)+[pivot]+quickSort(second,reverse)
#从1到999之间任选10个数字
lst=[randint(1,1000)for i in range(10)]
print(quickSort(lst)) """

#4.百分制转等级制的示例
"""def func(score):
    degree='DCBAAE'
    if score>100 or score<0:
        return 'wrong score,must between 0 and 100.'
    else:
        index=(score-60)//10
        if index>=0:
            return degree[index]
        else:
            return degree[-1]
print(func(10))"""

#5.面试资格确认
"""age=24
subject="计算机"
college="非重点"
if (age>25 and subject=="电子信息工程") or (college=="重点" and subject=="电子信息工程") or (age<=28 and subject=="计算机"):
    print("恭喜，您已经获得我公司的面试机会！")
else:
    print("抱歉，您未达到面试要求!")"""

#6.用户输入若干成绩，求所有成绩的总和。每输入一个成绩后询问是否继续输入下一个成绩，回答yes就继续输入下一个成绩，回答no就停止输入成绩
"""endFlag='yes'
s=0
while endFlag.lower()=='yes':
    x=input("请输入一个整数:")
#print(x)
    x=eval(x)    
    if isinstance(x,int) and 0<=x<=100:
        s=s+x
    else:
        print("不是数字或者不符合要求")
        endFlag=input('继续输入?(yes or no)')
    print('整数之和=',s)"""

#Python3.0以上的input函数返回的都是string字符串类型
"""x=input("请输入一个整数:")
print(type(x))
y=eval(x)
print(type(y))"""

#7.编写程序，判断某天是某年的第几天
"""import time

def demo(year,month,day):
    day_month=[31,28,31,30,31,30,31,31,30,31,30,31]  #每个月的天数
    if year%400==0 or (year%4==0 and year%100!=0):   #判断是否为闰年
        day_month[1]=29                              #闰年2月为29天
    if month==1:
        return day
    else:
        return sum(day_month[:month-1])+day

date=time.localtime()
year,month,day=date[:3]
print(demo(year,month,day))   #本程序于2019年10月19日写的此时是今年的第292天"""

#8.标准库datetime提供了timedelta对象可以方便地计算指定年、月、日、时、分、秒之前或之后的日期时间，还提供了
#返回结果中包含“今天是今年的第几天”“今天是本周的第几天”等答案的timetuple()函数，等等。
import datetime
Today=datetime.date.today()
print(Today)




























