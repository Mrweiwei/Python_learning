#检查并判断密码字符串的安全强度
import string
#定义检查函数
def check(pwd):
    #密码必须至少包含6个字符
    if not isinstance(pwd,str) or len(pwd)<6:
        return 'not suitable for password'
    #密码强度等级与包含字符种类的对应关系
    d={1:'weak',2:'below middle',3:'above middle',4:'strong'}
    #分别用来标记pwd是否有数字、小写字母、大写字母和指定的标点符号
    r=[False]*4

    for ch in pwd:
        #是否包含数字
        if not r[0] and ch in string.digits:
            r[0]=True
        #是否包含小写字母
        elif not r[1] and ch in string.ascii_lowercase:
            r[1]=True
        #是否包含大写字母
        elif not r[2] and ch in string.ascii_uppercase:
            r[2]=True
        #是否包含指定的标点符号
        elif not r[3] and ch in ',.!;<>':
            r[3]=True
        #统计包含的字符种类，返回密码强度
    return d.get(r.count(True),'error')

while True:
    pwd=input('请您输入您需要检查安全强度的密码：')
    print(check(pwd))
    s=input('是否需要继续校验(y/n)')
    if s=='n':
        break
        
