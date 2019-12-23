from faker import Faker
from faker.providers import BaseProvider
import random
import pymysql

fake=Faker("zh-CN")


class MyProvider(BaseProvider):
    def email_source(self):
        '''邮箱来源'''
        email_source=["163邮箱","阿里云邮箱","北京工业大学邮箱","126邮箱","QQ邮箱","189邮箱","21cn邮箱","Hotmail邮箱","新浪邮箱","沃邮箱"]
        return random.choice(email_source)
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
#创建表的字段。'''
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

try:
    for i in range(1000):
        #插入1000条数据
        # SQL 插入语句
        sql="""insert into qw_email_data(email_source,addresser,theme,time,user_name,email_detail)values("%s","%s","%s","%s","%s","%s")"""\
            %(fake.email_source(),fake.name(),fake.sentence(4),fake.date_this_year()," ","0")
        # 执行sql语句
        cursor.execute(sql)
    # 提交到数据库执行
    conn.commit()    
except Exception as e:
    # 如果发生错误则回滚
    conn.rollback()
    print(e)
else:
    print("数据插入成功！")   
#cursor.close()
# 关闭数据库连接
conn.close()























