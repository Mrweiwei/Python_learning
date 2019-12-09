#Python用format()方法进行字符串格式化的例子

print("The number {0:,} in hex is:{0:#x},the number {1} in oct os {1:#o}".format(5555,55))
#{0},{1}都是占位符，分别表示format函数里的第零个参数和第一个参数
#{0:,}第零位参数的位数用逗号隔开千位和万位  {0:#x}将第零位的参数转换成十六进制  #o表示八进制
print("The number {0} in hex is:{0:#x},the number {1} in oct os {1:#o}".format(5555,55))
#55太小所以没法逗号隔开
print("The number {1:,} in hex is:{1:#x},the number {0} in oct os {0:#o}".format(5555,55))
print("The number {1} in hex is:{1:#x},the number {0} in oct os {0:#o}".format(5555,55))

print("My name is {name},my age is {age},and my phoneNumber is {number}".format(name="魏巍",age=24,number=15227860591))
print("My name is {0},my age is {1},and my phoneNumber is {2}".format("魏巍",24,15227860591))

position=(5,8,13)
print("X:{0[0]};Y:{0[1]};Z:{0[2]}".format(position))#0相当于position，{position[0:3]} 切片、range函数和randrange都是左闭右开区间

weather=[("Monday","rain"),("Tuesday","sunny"),("Wednesday","sunny"),("Thursday","rain"),("Friday","cloudy")]
formatter="weather of  '{0[0]}'is '{0[1]}'".format
#formatter相当于做了一个例子接下来就是遍历输出
for item in map(formatter,weather):
    print(item)

#内置函数的方法实现：
for item in weather:
    print(formatter(item))





