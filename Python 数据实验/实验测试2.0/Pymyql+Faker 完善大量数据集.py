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
#创建表的字段。
'''sql="""
create table qw_test_data(
id int(32) PRIMARY KEY auto_increment,
order_id VARCHAR(50),
name VARCHAR(255) NULL,
num INT,
payway VARCHAR(50),
dealtime VARCHAR(50),
link_href VARCHAR(255) NULL,
money_thing VARCHAR(50),
uid VARCHAR(50),
user_name VARCHAR(50),
source_id VARCHAR(50),
category_id VARCHAR(50),
goods_brand VARCHAR(50)
)DEFAULT CHARSET=utf8,AUTO_INCREMENT = 1;"""
cursor.execute(sql)'''

#print(Goods_data.Goods_list[45776]["url"])
#for i in range(10):
#    print(Goods_data.外卖[i]["title"])

#切换中文输出
fake=Faker("zh-CN")
#添加自定义类
class MyProvider(BaseProvider):
    '''五大类库随机选取数据'''
    def 用(self):
        return random.choice(Goods_data.用)
    def 衣(self):
        return random.choice(Goods_data.衣)
    def 食(self):
        return random.choice(Goods_data.食)
    def 玩(self):
        return random.choice(Goods_data.玩)
    def 其它(self):
        return random.choice(Goods_data.其它)

    '''45个小类库中随机选取数据'''
    def 家用电器(self):
        return random.choice(Goods_data.家用电器)
    def 手机(self):
        return random.choice(Goods_data.手机)
    def 数码(self):
        return random.choice(Goods_data.数码)
    def 电脑周边(self):
        return random.choice(Goods_data.电脑周边)
    def 办公(self):
        return random.choice(Goods_data.办公)
    def 家具(self):
        return random.choice(Goods_data.家具)
    def 家居(self):
        return random.choice(Goods_data.家居)
    def 家装(self):
        return random.choice(Goods_data.家装)
    def 运营商(self):
        return random.choice(Goods_data.运营商)
    def 厨具(self):
        return random.choice(Goods_data.厨具)
    def 男装(self):
        return random.choice(Goods_data.男装)
    def 女装(self):
        return random.choice(Goods_data.女装)
    def 童装(self):
        return random.choice(Goods_data.童装)
    def 内衣(self):
        return random.choice(Goods_data.内衣)
    def 美妆个护(self):
        return random.choice(Goods_data.美妆个护)
    def 宠物(self):
        return random.choice(Goods_data.宠物)
    def 女鞋(self):
        return random.choice(Goods_data.女鞋)
    def 箱包(self):
        return random.choice(Goods_data.箱包)
    def 钟表(self):
        return random.choice(Goods_data.钟表)
    def 珠宝首饰(self):
        return random.choice(Goods_data.珠宝首饰)
    def 运动服饰(self):
        return random.choice(Goods_data.运动服饰)
    def 男鞋(self):
        return random.choice(Goods_data.男鞋)
    def 户外(self):
        return random.choice(Goods_data.户外)
    def 汽车(self):
        return random.choice(Goods_data.汽车)
    def 汽车用品(self):
        return random.choice(Goods_data.汽车用品)
    def 母婴(self):
        return random.choice(Goods_data.母婴)
    def 玩具乐器(self):
        return random.choice(Goods_data.玩具乐器)
    def 酒类(self):
        return random.choice(Goods_data.酒类)
    def 生鲜(self):
        return random.choice(Goods_data.生鲜)
    def 特产(self):
        return random.choice(Goods_data.特产)
    def 食物饮品(self):
        return random.choice(Goods_data.食物饮品)
    def 礼品鲜花(self):
        return random.choice(Goods_data.礼品鲜花)
    def 农资绿植(self):
        return random.choice(Goods_data.农资绿植)
    def 医疗保健(self):
        return random.choice(Goods_data.医疗保健)
    def 计生情趣(self):
        return random.choice(Goods_data.计生情趣)
    def 图书(self):
        return random.choice(Goods_data.图书)
    def 音像(self):
        return random.choice(Goods_data.音像)
    def 机票(self):
        return random.choice(Goods_data.机票)
    def 电影票(self):
        return random.choice(Goods_data.电影票)
    def 旅游(self):
        return random.choice(Goods_data.旅游)
    def 酒店(self):
        return random.choice(Goods_data.酒店)
    def 理财(self):
        return random.choice(Goods_data.理财)
    def 外卖(self):
        return random.choice(Goods_data.外卖)
    def 其它(self):
        return random.choice(Goods_data.其它)
    def 网游(self):
        return random.choice(Goods_data.网游)
    def 保险(self):
        return random.choice(Goods_data.保险)

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



def order():
    '''定义生成一个16位的订单号'''
    str=""
    for i in range(1,17):        
        ch = chr(random.randrange(ord('1'), ord('9') + 1))
        str += ch
    return str

def Data_Select(uid,username,n,c,u,d,p,o,l):
    '''定义为用户选取相应需要的数据的函数'''
    #range函数中不支持float类型，必须是int类型
    ci=int(n*c)
    ui=int(n*u)
    di=int(n*d)
    pi=int(n*p)
    oi=int(n*o)
    li=int(n*l)
    #从衣服库中选数据并插入数据库中
    for i in range(ci):
        dic=fake.美妆个护()
        a=dic["title"]
        b=dic["price"]
        c=dic["url"]
        d=dic["category_id"]
        e=dic["source_id"]
        #print(type(dic["title"]))
        # SQL 插入语句
        '''sql=cursor.mogrify("""insert into qw_jingdong_data(order_id,goods,num,money,payway,time,link_href,position) values('%s',"%s",%d,"%s",'%s','%s',"%s",'%s')"""\
            %(order(),a,1,b,fake.payway(),fake.date_this_year(),c,fake.position()))
        print(sql)
        '''
        sql="""insert into qw_test_data(order_id,name,num,payway,dealtime,link_href,money_thing,uid,user_name,source_id,category_id,goods_brand)values('%s',"%s",%d,'%s','%s',"%s","%s",'%s','%s','%s','%s','%s')"""\
            %(order(),a,1,fake.payway(),fake.date_time_between(start_date="-90d", end_date="-59d"),c,b,uid,username,e,d,'')
        # 执行sql语句
        cursor.execute(sql)
     #从用库中选数据并插入数据库中
    for i in range(ui):
        dic=fake.食物饮品()
        a=dic["title"]
        b=dic["price"]
        c=dic["url"]
        d=dic["category_id"]
        e=dic["source_id"]
        #print(type(dic["title"]))
        # SQL 插入语句
        '''sql=cursor.mogrify("""insert into qw_jingdong_data(order_id,goods,num,money,payway,time,link_href,position) values('%s',"%s",%d,"%s",'%s','%s',"%s",'%s')"""\
            %(order(),a,1,b,fake.payway(),fake.date_between(start_date="-1y", end_date="now"),c,fake.position()))
        print(sql)
        '''
        sql="""insert into qw_test_data(order_id,name,num,payway,dealtime,link_href,money_thing,uid,user_name,source_id,category_id,goods_brand)values('%s',"%s",%d,'%s','%s',"%s","%s",'%s','%s','%s','%s','%s')"""\
            %(order(),a,1,fake.payway(),fake.date_time_between(start_date="-90d", end_date="-59d"),c,b,uid,username,e,d,'')
        # 执行sql语句
        cursor.execute(sql)
     #从食物库中选数据并插入数据库中
    for i in range(di):
        dic=fake.外卖()
        a=dic["title"]
        b=dic["price"]
        c=dic["url"]
        d=dic["category_id"]
        e=dic["source_id"]
        #print(type(dic["title"]))
        # SQL 插入语句
        '''sql=cursor.mogrify("""insert into qw_jingdong_data(order_id,goods,num,money,payway,time,link_href,position) values('%s',"%s",%d,"%s",'%s','%s',"%s",'%s')"""\
            %(order(),a,1,b,fake.payway(),fake.date_this_year(),c,fake.position()))
        print(sql)
        '''
        sql="""insert into qw_test_data(order_id,name,num,payway,dealtime,link_href,money_thing,uid,user_name,source_id,category_id,goods_brand)values('%s',"%s",%d,'%s','%s',"%s","%s",'%s','%s','%s','%s','%s')"""\
            %(order(),a,1,fake.payway(),fake.date_time_between(start_date="-90d", end_date="-59d"),c,b,uid,username,e,d,'')
        # 执行sql语句
        cursor.execute(sql)
     #从玩库中选数据并插入数据库中
    for i in range(pi):
        dic=fake.衣()
        a=dic["title"]
        b=dic["price"]
        c=dic["url"]
        d=dic["category_id"]
        e=dic["source_id"]
        #print(type(dic["title"]))
        # SQL 插入语句
        '''sql=cursor.mogrify("""insert into qw_jingdong_data(order_id,goods,num,money,payway,time,link_href,position) values('%s',"%s",%d,"%s",'%s','%s',"%s",'%s')"""\
            %(order(),a,1,b,fake.payway(),fake.date_this_year(),c,fake.position()))
        print(sql)
        '''
        sql="""insert into qw_test_data(order_id,name,num,payway,dealtime,link_href,money_thing,uid,user_name,source_id,category_id,goods_brand)values('%s',"%s",%d,'%s','%s',"%s","%s",'%s','%s','%s','%s','%s')"""\
            %(order(),a,1,fake.payway(),fake.date_time_between(start_date="-90d", end_date="-59d"),c,b,uid,username,e,d,'')
        # 执行sql语句
        cursor.execute(sql)
    #从其它库中选数据并插入数据库中
    for i in range(oi):
        dic=fake.图书()
        a=dic["title"]
        b=dic["price"]
        c=dic["url"]
        d=dic["category_id"]
        e=dic["source_id"]
        #print(type(dic["title"]))
        # SQL 插入语句
        '''sql=cursor.mogrify("""insert into qw_jingdong_data(order_id,goods,num,money,payway,time,link_href,position) values('%s',"%s",%d,"%s",'%s','%s',"%s",'%s')"""\
            %(order(),a,1,b,fake.payway(),fake.date_this_year(),c,fake.position()))
        print(sql)
        '''
        sql="""insert into qw_test_data(order_id,name,num,payway,dealtime,link_href,money_thing,uid,user_name,source_id,category_id,goods_brand)values('%s',"%s",%d,'%s','%s',"%s","%s",'%s','%s','%s','%s','%s')"""\
            %(order(),a,1,fake.payway(),fake.date_time_between(start_date="-90d", end_date="-59d"),c,b,uid,username,e,d,'')
        # 执行sql语句
        cursor.execute(sql)
    for i in range(li):
        dic=fake.其它()
        a=dic["title"]
        b=dic["price"]
        c=dic["url"]
        d=dic["category_id"]
        e=dic["source_id"]
        #print(type(dic["title"]))
        # SQL 插入语句
        '''sql=cursor.mogrify("""insert into qw_jingdong_data(order_id,goods,num,money,payway,time,link_href,position) values('%s',"%s",%d,"%s",'%s','%s',"%s",'%s')"""\
            %(order(),a,1,b,fake.payway(),fake.date_this_year(),c,fake.position()))
        print(sql)
        '''
        sql="""insert into qw_test_data(order_id,name,num,payway,dealtime,link_href,money_thing,uid,user_name,source_id,category_id,goods_brand)values('%s',"%s",%d,'%s','%s',"%s","%s",'%s','%s','%s','%s','%s')"""\
            %(order(),a,1,fake.payway(),fake.date_time_between(start_date="-90d", end_date="-59d"),c,b,uid,username,e,d,'')
        # 执行sql语句
        cursor.execute(sql)
    # 提交到数据库执行
    conn.commit()   
try:
    
    #运行构造的函数参数的顺序分别是uid,username,分别从衣,用,食,玩,其他取数据的比例
    Data_Select("1","admin",100,0.25,0.13,0.2,0.15,0.06,0.21)
    
except Exception as e:
    # 如果发生错误则回滚
    conn.rollback()
    print(e)
else:
    print("数据插入成功！")   
#cursor.close()
# 关闭数据库连接
conn.close()






















