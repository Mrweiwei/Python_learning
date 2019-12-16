#PyMySQL 是在 Python3.x 版本中用于连接 MySQL 服务器的一个库
import pymysql
import random
#Faker 是一个可以让你生成伪造数据的Python包。
from faker import Faker
from faker.providers import BaseProvider
import Goods_data

#print(Goods_data.Goods_list[0]["title"])
# 打开数据库连接
conn=pymysql.connect(
    host="localhost",
    port=3306,
    user='root',
    password='',
    db="sphider",
    charset="utf8"
    )
#使用 cursor() 方法创建一个游标对象 cursor
#category_id VARCHAR(50),
cursor=conn.cursor()
#创建表的字段。'''
'''sql="""
create table qw_jingdong_data(
id int(32) PRIMARY KEY auto_increment,
order_id VARCHAR(50),
goods VARCHAR(255),
num INT,
money VARCHAR(50),
payway VARCHAR(50),
time VARCHAR(50),
link_href VARCHAR(255) NULL,
position VARCHAR(50)
)DEFAULT CHARSET=utf8,AUTO_INCREMENT = 1;"""
cursor.execute(sql)'''

#print(Goods_data.Goods_list[45776]["url"])

#切换中文输出
fake=Faker("zh-CN")
#添加自定义类
class MyProvider(BaseProvider):
    def goods(self):
        return random.choice(Goods_data.Goods_list)

    def position(self):
        '''地点类'''
        position=['百度糯米',
                  '百度外卖',
                  '必胜客',
                  '当当网',
                  '达美乐比萨',
                  '大众点评',
                  '饿了么',
                  '1号店',
                  '凡客诚品',
                  '国美电器',
                  '京东',
                  '聚美优品',
                  '酒仙网',
                  '吉野家',
                  '肯德基',
                  '麦当劳',
                  '驴妈妈旅游网',
                  '蘑菇街',
                  '美团网',
                  '美团外卖',
                  '苏宁易购',
                  '淘宝网',
                  '唯品会',
                  '网易考+拉海购',
                  '亚马逊',
                  '我买网']
        return random.choice(position)

    def payway(self):
        '''支付方式类'''
        payway=['在线支付/白条',
                '在线支付/花呗',
                '在线支付/银行卡',
                '在线支付/微信']
        return random.choice(payway)

fake.add_provider(MyProvider)

'''dic=fake.goods()
title=dic["title"]
price=dic["price"]
url=dic["url"]
print(type(price))'''

try:
    def order():
        '''定义生成一个16位的订单号'''
        str=""
        for i in range(1,17):        
            ch = chr(random.randrange(ord('1'), ord('9') + 1))
            str += ch
        return str

    for i in range(1000):
        #插入1000条数据
        dic=fake.goods()
        a=dic["title"]
        b=dic["price"]
        c=dic["url"]
        #print(type(dic["title"]))
        # SQL 插入语句
        '''sql=cursor.mogrify("""insert into qw_jingdong_data(order_id,goods,num,money,payway,time,link_href,position) values('%s',"%s",%d,"%s",'%s','%s',"%s",'%s')"""\
            %(order(),a,1,b,fake.payway(),fake.date_this_year(),c,fake.position()))
        print(sql)
        '''
        sql="""insert into qw_jingdong_data(order_id,goods,num,money,payway,time,link_href,position)values('%s',"%s",%d,"%s",'%s','%s',"%s",'%s')"""\
            %(order(),a,1,b,fake.payway(),fake.date_this_year(),c,fake.position())
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

























