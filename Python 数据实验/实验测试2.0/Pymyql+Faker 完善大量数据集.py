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

#模拟四个不同的用户(test1,test2,test3,test4)
#模拟test1用户的数据:衣服数据1000个，用500个，食500个，玩250个，其它250个
    for i in range(1000):
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
            %(order(),a,1,fake.payway(),fake.date_this_year(),c,b,'41','test1',e,d,'')
        # 执行sql语句
        cursor.execute(sql)
    for i in range(500):
        dic=fake.用()
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
            %(order(),a,1,fake.payway(),fake.date_this_year(),c,b,'41','test1',e,d,'')
        # 执行sql语句
        cursor.execute(sql)
    for i in range(500):
        dic=fake.食()
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
            %(order(),a,1,fake.payway(),fake.date_this_year(),c,b,'41','test1',e,d,'')
        # 执行sql语句
        cursor.execute(sql)
    for i in range(250):
        dic=fake.玩()
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
            %(order(),a,1,fake.payway(),fake.date_this_year(),c,b,'41','test1',e,d,'')
        # 执行sql语句
        cursor.execute(sql)
    for i in range(250):
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
            %(order(),a,1,fake.payway(),fake.date_this_year(),c,b,'41','test1',e,d,'')
        # 执行sql语句
        cursor.execute(sql)
#模拟test2用户的数据:食1000个，用500个，衣500个，玩250个，其它250个
    for i in range(1000):
        #插入1000条数据
        dic=fake.食()
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
            %(order(),a,1,fake.payway(),fake.date_this_year(),c,b,'42','test2',e,d,'')
        # 执行sql语句
        cursor.execute(sql)
    for i in range(500):
        dic=fake.用()
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
            %(order(),a,1,fake.payway(),fake.date_this_year(),c,b,'42','test2',e,d,'')
        # 执行sql语句
        cursor.execute(sql)
    for i in range(500):
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
            %(order(),a,1,fake.payway(),fake.date_this_year(),c,b,'42','test2',e,d,'')
        # 执行sql语句
        cursor.execute(sql)
    for i in range(250):
        dic=fake.玩()
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
            %(order(),a,1,fake.payway(),fake.date_this_year(),c,b,'42','test2',e,d,'')
        # 执行sql语句
        cursor.execute(sql)
    for i in range(250):
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
            %(order(),a,1,fake.payway(),fake.date_this_year(),c,b,'42','test2',e,d,'')
        # 执行sql语句
        cursor.execute(sql)
#模拟test3用户的数据:用1000个，食500个，衣500个，玩250个，其它250个
    for i in range(1000):
        #插入1000条数据
        dic=fake.用()
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
            %(order(),a,1,fake.payway(),fake.date_this_year(),c,b,'43','test3',e,d,'')
        # 执行sql语句
        cursor.execute(sql)
    for i in range(500):
        dic=fake.食()
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
            %(order(),a,1,fake.payway(),fake.date_this_year(),c,b,'43','test3',e,d,'')
        # 执行sql语句
        cursor.execute(sql)
    for i in range(500):
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
            %(order(),a,1,fake.payway(),fake.date_this_year(),c,b,'43','test3',e,d,'')
        # 执行sql语句
        cursor.execute(sql)
    for i in range(250):
        dic=fake.玩()
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
            %(order(),a,1,fake.payway(),fake.date_this_year(),c,b,'43','test3',e,d,'')
        # 执行sql语句
        cursor.execute(sql)
    for i in range(250):
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
            %(order(),a,1,fake.payway(),fake.date_this_year(),c,b,'43','test3',e,d,'')
        # 执行sql语句
        cursor.execute(sql)
#模拟test4用户的数据:玩1000个，用500个，食500个，衣250个，其它250个
    for i in range(1000):
        #插入1000条数据
        dic=fake.玩()
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
            %(order(),a,1,fake.payway(),fake.date_this_year(),c,b,'44','test4',e,d,'')
        # 执行sql语句
        cursor.execute(sql)
    for i in range(500):
        dic=fake.用()
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
            %(order(),a,1,fake.payway(),fake.date_this_year(),c,b,'44','test4',e,d,'')
        # 执行sql语句
        cursor.execute(sql)
    for i in range(500):
        dic=fake.食()
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
            %(order(),a,1,fake.payway(),fake.date_this_year(),c,b,'44','test4',e,d,'')
        # 执行sql语句
        cursor.execute(sql)
    for i in range(250):
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
            %(order(),a,1,fake.payway(),fake.date_this_year(),c,b,'44','test4',e,d,'')
        # 执行sql语句
        cursor.execute(sql)
    for i in range(250):
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
            %(order(),a,1,fake.payway(),fake.date_this_year(),c,b,'44','test4',e,d,'')
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













