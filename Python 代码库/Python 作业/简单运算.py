List = input("请输入一个列表：").split( )
num = input("请输入两个整数：").split( ) 
num.sort()
print(List[int(num[0]):int(num[1])+1])
