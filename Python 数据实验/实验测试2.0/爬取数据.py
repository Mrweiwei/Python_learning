import requests
import re
import time
import csv
import pymysql

conn=pymysql.connect(
    host="localhost",
    port=3306,
    user='root',
    password='',
    db="runoob_db",
    charset="utf8"
    )
cursor=conn.cursor()
#建表
'''sql="""
create table Goods_data(
id int PRIMARY KEY auto_increment,
price VARCHAR(255),
name VARCHAR(50),
location VARCHAR(255),
sales VARCHAR(50)
)DEFAULT CHARSET=utf8"""
cursor.execute(sql)'''

def getHTMLText(url):
    try:
    #每次登陆淘宝，淘宝都会以加密方式返回登陆账号和密码信息，如果使用程序访问的话，需要发送post请求，这时需要发送cookie，以实现自动登录。请使用自己的cookie，复制到header字典中。
        header={"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
"cookie":"miid=1547288390134411071; t=816c37d275550ae0c70552305a3e6348; cna=DnUIFt3LGRcCAdvtcAXHl8EG; lgc=vampireww158; tracknick=vampireww158; tg=0; mt=ci=6_1; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; v=0; _tb_token_=39587ea1e01de; csg=30e8125b; dnk=vampireww158; existShop=MTU3NTg3MzQ4OA%3D%3D; _cc_=UtASsssmfA%3D%3D; _l_g_=Ug%3D%3D; sg=865; _nk_=vampireww158; uc1=cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&cookie21=VFC%2FuZ9aiKCaj7AzMHh1&cookie15=UIHiLt3xD8xYTw%3D%3D&existShop=false&pas=0&cookie14=UoTbmEOrgdf%2B0A%3D%3D&tag=8&lng=zh_CN; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; l=dBTcgunPq0FFJmsyBOCanurza77OSIRYYuPzaNbMi_5pv6T_5vbOkHGzbF96VjS1GqTB4NSLztv9-etkZwA5MK--g3frJXdmCeyIj1knExf..; isg=BBUVQEPY5LnokcBF7Nw-I_AmJBEPushOVNDI-Je60Qzb7jXgX2LZ9COsvLJ9deHc"}
        r = requests.get(url,headers=header,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
    

def parsePage(ilt,html):
    try:
    #请百度搜索正则表达式的菜鸟教程，勤加练习，必有大成。
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        loc = re.findall(r'\"item_loc\"\:\".*?\"',html)
        sale = re.findall(r'\"view_sales\"\:\"[\d\.]*.*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            location = eval(loc[i].split(':')[1])
            sales = eval(sale[i].split(':')[1])
            ilt.append([price,title,location,sales])
    except:
        print("")

def printGoodsList(ilt):
    #tplt = "{:4}\t{:6}\t{:8}\t{:8}\t{:8}"
    #print(tplt.format("序号","价格","商品名称","商品地址","付款数量"))
    for g in ilt:
        sql="""insert into goods_data(price,name,location,sales)values('%s','%s','%s','%s')"""%(g[0],g[1],g[2],g[3])
        cursor.execute(sql)
    conn.commit()
def main(goods,depth):
    start_url='https://s.taobao.com/search?q='+goods
    infoList =[]
    for i in range(depth):
        try:
            url = start_url + '&s='+ str(44*i)
           # 下面是我的网址简化过程，最好学习一下。
#1、https://s.taobao.com/search?q=圆珠笔&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20190826&ie=utf8&p4ppushleft=1%2C48&s=0
#2、https://s.taobao.com/search?q=圆珠笔&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20190826&ie=utf8&p4ppushleft=1%2C48
#3、https://s.taobao.com/search?q=圆珠笔
#4、这个网址就可以实现我们需要的数据返回。
            html= getHTMLText(url)
            parsePage(infoList,html)
        except:
                continue
    #print(html)        
    printGoodsList(infoList)
    

#实现超级简单的用户交互，想爬取什么就爬取什么
goods=input("请输入你需要搜索的商品：")
#本文仅供学习，爬虫深度的设置，请理性设置
depth=int(input("请输入需要爬取的页数（请尝试在淘宝中搜索该商品关键词，查看返回页码，请理性设置爬虫深度）："))
#传参，需把外部参数传入main函数中。
main(goods,depth)
#提醒
print("数据爬取结束")
time.sleep(10)
conn.close()
