from faker import Faker
from faker.providers import BaseProvider
import random
import pymysql
import Mail_data

fake=Faker("zh-CN")


class MyProvider(BaseProvider):
    def email_source(self):
        '''邮箱来源'''
        email_source=["163邮箱","阿里云邮箱","北京工业大学邮箱","126邮箱","QQ邮箱","189邮箱","21cn邮箱","Hotmail邮箱","新浪邮箱","沃邮箱"]
        return random.choice(email_source)
    def 正常邮箱(self):
        '''正常邮箱主题'''
        return random.choice(Mail_data.正常邮箱)
    def 垃圾邮箱(self):
        '''垃圾邮箱主题'''
        return random.choice(Mail_data.垃圾邮箱)
    
fake.add_provider(MyProvider)

# 打开数据库连接
conn=pymysql.connect(
    host="localhost",
    port=3306,
    user='root',
    password='',
    db="sphider",
    charset="utf8"
    )

#print(fake.sentence(4))
cursor=conn.cursor()
#创建表的字段
'''sql="""
create table qw_email_data(
id int(32) PRIMARY KEY auto_increment,
email_source VARCHAR(50),
addresser VARCHAR(50),
theme VARCHAR(50),
time VARCHAR(50),
user_name VARCHAR(50),
email_detail VARCHAR(50)
)DEFAULT CHARSET=utf8,AUTO_INCREMENT = 1;"""
cursor.execute(sql)'''

def Email_Select(username,n,a,b):
    '''定义为用户分配正常邮件和垃圾邮件的比例'''
    N=int(n*a)
    C=int(n*b)
    for i in range(N):
        # SQL 插入语句
        dic=fake.正常邮箱()
        theme=dic["theme"]
        category_id=dic["category_id"]
        sql="""insert into qw_email_data(email_source,addresser,theme,time,user_name,email_detail)values("%s","%s","%s","%s","%s","%s")"""\
            %(fake.email_source(),fake.name(),theme,fake.date_time_between(start_date="-90d", end_date="-59d"),username,category_id)
        # 执行sql语句
        cursor.execute(sql)

    for i in range(C):
        # SQL 插入语句
        dic=fake.垃圾邮箱()
        theme=dic["theme"]
        category_id=dic["category_id"]
        sql="""insert into qw_email_data(email_source,addresser,theme,time,user_name,email_detail)values("%s","%s","%s","%s","%s","%s")"""\
            %(fake.email_source(),fake.name(),theme,fake.date_time_between(start_date="-90d", end_date="-59d"),username,category_id)
        # 执行sql语句
        cursor.execute(sql)
    # 提交到数据库执行
    conn.commit()  



try:
#调用函数：第一个参数是被分配邮件的用户，n是总数量，a是正常邮件的比例数，b是垃圾邮件的比例数
    Email_Select("admin",1000,0.6,.04)
except Exception as e:
    # 如果发生错误则回滚
    conn.rollback()
    print(e)
else:
    print("数据插入成功！")   
#cursor.close()
# 关闭数据库连接
conn.close()



#测试代码：
'''for i in range(100):
    print(fake.email_theme())'''





















