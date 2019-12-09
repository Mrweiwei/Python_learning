import mysql.connector
from faker import Faker
import random
from faker.providers import BaseProvider
'''创建表的最后一定要添加DEFAULT CHARSET=utf8，否则插入的数据会出现乱码的情况
所以创建shopping_data表的时候一定在后面加上这句话'''
#mycursor.execute("CREATE TABLE sites (id INT AUTO_INCREMENT PRIMARY KEY, time VARCHAR(255), position VARCHAR(255),goods VARCHAR(255))DEFAULT CHARSET=utf8")
mydb = mysql.connector.connect(
  host="localhost",       # 数据库主机地址
  user="root",    # 数据库用户名
  passwd="",   # 数据库密码
  database="runoob_db"
)
fake = Faker('zh_CN')
class MyProvider(BaseProvider):
    def goods(self):
        goods=['防水迷你夜视接手机望远镜','智能定时开关插排','智能手环手表','家用无线门铃','智能蓝牙偏光眼镜','迷你手机小话筒','迷你金属小钢炮','智能体重秤','智能蓝牙防丢器','智能人体感应小夜灯']
        return random.choice(goods)
    def position(self):
        position=['百度糯米','百度外卖','必胜客','当当网','达美乐比萨','大众点评','饿了么','1号店','凡客诚品','国美电器','京东','聚美优品','酒仙网','吉野家','肯德基','麦当劳','驴妈妈旅游网','蘑菇街','美团网','美团外卖','苏宁易购','淘宝网','唯品会','网易考拉海购','亚马逊','我买网']
        return random.choice(position)
fake.add_provider(MyProvider)

mycursor = mydb.cursor()
val =[]
#mycursor.execute("CREATE TABLE shopping_list(id INT AUTO_INCREMENT PRIMARY KEY, time VARCHAR(255), position VARCHAR(255),goods VARCHAR(255))DEFAULT CHARSET=utf8")
sql="INSERT INTO shopping_list(time,position,goods) VALUES(%s,%s,%s)"
for i in range(1,10000):
    val.append((fake.date_this_month(),fake.position(),fake.goods()))

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "记录插入成功。")













