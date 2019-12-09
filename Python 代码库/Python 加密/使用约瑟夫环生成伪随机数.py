'''问题描述：

            使用约瑟夫环生成伪随机数
   技术要点：
            （1）在Python中自定义类；
            （2）使得自定义类的对象支持内置函数next()
            （3）根据系统时间对数据进行乱序的思路'''
from time import time,sleep

class RandomInteger:
    #构造方法，初始化
    def __init__(self,start,stop,seed,k):
        assert isinstance(start,int),'start必须为整数'
        assert isinstance(stop,int)and stop>start,'stop必须为大于start的整数'
        assert isinstance(seed,int)and seed in range(start,stop),'seed必须介于[start,stop)区间的整数'
        assert isinstance(k,int)and k<stop-start,'k必须为小于stop-start的整数'
        self.data=list(range(start,stop))
        #把初始数据随机打乱顺序，交换100个数字的位置
        length=stop-start
        for _ in range(100):
            sleep(0.001)
            #根据当前时间的小数部分决定交换哪两个位置的值
            currentIndex=int(str(time()).split('.')[1])%length+1
            if currentIndex==length:
                currentIndex=length-1
            self.data[currentIndex],self.data[length-currentIndex]=(self.data[length-currentIndex],self.data[currentIndex])
        self.data=self.data[seed:]+self.data[:seed]
        self.k=k

    #通过内置函数next()索要随机数时，自动调用__next__()方法
    def __next__(self):
        #变换列表中的数字顺序，然后返回第一个数字
        self.data=self.data[self.k:]+self.data[:self.k]
        return self.data[0]

r=RandomInteger(1,38,7,6)
#获取100个伪随机数
for _ in range(100):
    print(next(r))


























    
