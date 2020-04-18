'''使用协同过滤算法进行电影推荐'''

#协同过滤算法常用于商品推荐或者类似的场合，根据用户之间或商品之间的相似性进行精准推荐。协同过滤算法可以分为基于用户
#的协同过滤算法和基于商品的协同过滤算法。

'''以电影推荐为例，假设用户1喜欢看电影A、B、C、D、G，用户2喜欢看电影A、D、E、F，用户3喜欢看电影A、B、D，现在用户3
像在看一部没看过的电影，向用户1和用户2寻求推荐。'''

#在扩展库sklearn中并没有提供协同过滤算法的实现，下面代码直接使用Python编程实现

from random import randrange

#模拟历史电影打分数据，共10个用户，每个用户打分的电影数量不等
data={'user'+str(i):{'film'+str(randrange(1,15)):randrange(1,6) for j in range(randrange(3,10))}for i in range
      (10)}

#寻求推荐的用户对电影打分的数据
user={'film'+str(randrange(1,15)):randrange(1,6) for i in range(5)}

#最相似的用户及其对电影的打分情况
#两个最相似的用户共同打分的电影最多，同时所有电影打分差值的平方和最小
rule=lambda item:(-len(item[1].keys()&user),sum(((item[1].get(film)-user.get(film))**2 for film in user.keys()\
                                               &item[1].keys())))
similarUser,films=min(data.items(),key=rule)
#输入信息以便验证，每行数据有3列
#分别为该用户与当前用户共同打分的电影数量、打分差的平方和、该用户打分数据
print('Known data'.center(50,'='))
for item in data.items():
    print(len(item[1].keys()&user.keys()),sum(((item[1].get(film)-user.get(film))**2 for film in user.keys()\
                                              &item[1].keys())),item,sep=':')



print('current user'.center(50,'='),user,sep='\n')
print('most similar user and his films'.center(50,'='))
print(similarUser,films,sep=':')
print('recommended film'.center(50,'='))
#在当前用户没看见过的电影选择打分最高的进行推荐
print(max(films.keys()-user.keys(),key=lambda film:films[film]))




















