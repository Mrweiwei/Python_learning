#利用字符串的方法制作映射表（相当于秘钥）
import string
def Caesar(s,k):                      #第一个形参相当于要加密的明文，K表示循环左移的位数
    lower=string.ascii_lowercase      #小写字母
    upper=string.ascii_uppercase      #大写字母
    before=string.ascii_letters
    after=lower[k:]+lower[:k]+upper[k:]+upper[:k]
    table=''.maketrans(before,after)  #创建映射表
    print(s.translate(table))         #返回加密玩的密文

while True:
    s=input("请您输入需要加密的明文(必须是由26个字母组成的)：")
    Caesar(s,3)   
    d=input("想继续加密吗？(y/n)")
    if d=='n':
        break
    
