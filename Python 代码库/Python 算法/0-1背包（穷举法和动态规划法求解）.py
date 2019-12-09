'''问题描述：现有若干重量和价值不相同的物品以及1个固定容量的背包，可以任意选择多个物品放入背包，如何让背包里装入的物品
总价值最大？假设物品从0开始编号，输出在不超过物品总质量的前提下放入背包能够使得物品总价值最大的物品的编号。'''

from random import sample
from itertools import combinations,permutations

#穷举法
def bag01_1(volume,price,weight):
    #背包容量必须大于0，并且保存物品价值和重量的列表一样长
    assert volume>0
    lenPrice=len(price)
    assert lenPrice==len(weight)
    #总容量不超过背包承受能力的所有组合的物品索引
    possibleCombs=[]
    for k in range(1,len(price)+1):
        possibleCombs.extend(filter(lambda item:sum(weight[i] for i in item)<=volume,combinations(range(lenPrice),k)))
        #在所有可能的组合中寻找总价值最大的组合，返回放进包里的物品的索引
        index=max(possibleCombs,key=lambda item:sum((price[i] for i in item)))
        return index

#穷举法
def bag01_2(volume,price,weight):
    #理想值，[最大价值，（最大价值的物品）]
    max_comb=[0,[]]
    #最终放进包里的必然是所有物品的某个全排列的前面几项
    #约束条件是放进包里的物品总质量不超过包的最大承重
    #满足约束条件的物品组合中，总价值最大的位最终结果
    for perm in permutations(zip(weight,price),len(weight)):
        temp_price,temp_weight=0,0
        for index,(w,p) in enumerate(perm):
            temp_weight=temp_weight+w
            if temp_weight>volume:
                break
            temp_price=temp_price+p
            #选择法
            if temp_price>max_comb[0]:
                max_comb=[temp_price,perm[:index]]
        #返回放进包里的物品的索引，假设所有物品的重量都不一样
        return tuple((weight.index(item[0]) for item in max_comb[1]))

#动态规划
def bag01_3(volume,price,weight):
    #实际物品数量
    num=len(weight)
    price=[0]+price
    weight=[0]+weight
    #填表
    #行索引表示第几个物品，从1开始对实际物品进行编号
    #列索引
    value=[]
    for _ in range(num+1):
        value.append([0]*(volume+1))
    for i in range(1,num+1):
        for j in range(1,volume+1):
            if j <weight[i]:
                value[i][j]=value[i-1][j]
            else:
                if value[i-1][j]>value[i-1][j-weight[i]]+price[i]:
                    value[i][j]=value[i-1][j]
                else:
                    value[i][j]=value[i-1][j-weight[i]]+price[i]

    #输出填表结果
    print('='*20)
    print('i/j',*map(lambda j:'%4d'%j,range(volume+1)),sep='')
    for irow,row in enumerate(value):
        print('%4d'%irow,end='')
        for col in row:
            print('%4d'%col,sep='',end='')
        print('\n')
    print('='*20)
    #根据填表结果查找放进包里的物品的索引
    index=[]
    def find(i,j):
        if i>=0:
            if value[i][j]==value[i-1][j]:
                find(i-1,j)
            elif j-weight[i]>=0 and value[i][j]==value[i-1][j-weight[i]]+price[i]:
                index.append(i)
                find(i-1,j-weight[i])
    find(num,volume)
    #原列表中物品编号从0开始，所以减1后得到实际物品索引
    index=[n-1 for n in index]
    return tuple(sorted(index))

#背包容量
volume=40
#物品数量
k=7
#物品重量
weight=sample(range(1,volume//2),k)
#物品价值
price=sample(range(1,100),k)
print(f'weight={weight}\nprice={price}')
print(bag01_1(volume,price,weight))
print(bag01_2(volume,price,weight))
print(bag01_3(volume,price,weight))
















































    
    























    
