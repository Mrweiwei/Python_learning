#模拟发红包
import random

def Hongbao(total,num):
    #total表示拟发红包总金额
    #num表示拟发红包数量
    each=[]
    #已发红包总金额
    already=0

    for i in range(1,num):
        #为当前抢红包的人随机分配金额
        #至少给剩下的人留一分钱
        t=random.randint(1,(total-already)-(num-i))
        each.append(t)
        already=already+t
    #剩余所有前发给最后一个人
    each.append(total-already)
    return each

if __name__=='__main__':
    total=50
    num=5
    #模拟30次
    for i in range(30):
        each=Hongbao(total,num)
        print(each)
