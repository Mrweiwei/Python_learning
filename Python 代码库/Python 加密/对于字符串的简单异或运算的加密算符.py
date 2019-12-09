#编写函数实现字符串加密和解密，循环使用指定密钥，采用简单的异或算法(这个算法有问题)
def crypt(source,key):
    from itertools import cycle
    result=''
    temp=cycle(key)
    for ch in source:
        result=result+chr(ord(ch)^ord(next(temp)))
    return result

source='Shandong Institute of Business and Technology'
key='Dong Fuguo'
Encrypt=crypt(source,key)
Decrypt=crypt(Encrypt,key)
print(Encrypt)
print(Decrypt)
