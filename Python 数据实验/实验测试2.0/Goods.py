#从数据库中导出数据并构造商品列表
import pymysql

# 打开数据库连接
conn = pymysql.connect("localhost","root","","tb_data" )
# 使用cursor()方法获取操作游标 
cursor =conn.cursor()
# SQL 查询语句
sql = "SELECT * FROM TB_DATA"
try:
    #执行SQL语句
    cursor.execute(sql)
    #获取所有记录列表
    results=cursor.fetchall()
    Shopping_list=[]
    Category_id_list=[]
    for row in results:
        Shopping_list.append(row[1])
        Category_id_list.append(row[4])
        #print(Category_id)

except:
    print ("Error: unable to fetch data")
# 关闭数据库连接
conn.close()
#print(Shopping_list)


