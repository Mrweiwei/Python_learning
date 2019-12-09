#在循环中尽量引用局部变量，因为局部变量的查询和访问速度比全局变量略快
import time
import math
start=time.time()  #获取当前时间
for i in range(100000):
    math.sin(i)
print('全局变量使用的时间为:',time.time()-start)  #输出所用的时间
loc_sin=math.sin
start=time.time()
for i in range(100000):
    loc_sin(i)
print('局部变量使用的时间为:',time.time()-start)

print("这段代码中的全部的局部变量是",locals())
print("这段代码中的全部的全局变量是",globals())   
  


