import requests
import re
import time
import csv


def getHTMLText(url):
    try:
    #每次登陆淘宝，淘宝都会以加密方式返回登陆账号和密码信息，如果使用程序访问的话，需要发送post请求，这时需要发送cookie，以实现自动登录。请使用自己的cookie，复制到header字典中。
        header={"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
"cookie":“输入你的cookie”}
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
    tplt = "{:4}\t{:6}\t{:8}\t{:8}\t{:8}"
    print(tplt.format("序号","价格","商品名称","商品地址","付款数量"))
    output_list=["序号","价格","商品名称","商品地址","付款数量"]
    #存储路径需根据需要更改
    with open('str(goods)+'（'+str(depth*48)+'条数据）'+'.csv',"a+",encoding='GB18030',newline='') as csvfile:
        	w=csv.writer(csvfile)
        	w.writerow(output_list)
        	csvfile.close()
    count=0
    for g in ilt:
        count = count+1
        print(tplt.format(count,g[0],g[1],g[2],g[3]))
        out_putlist=[count,g[0],g[1],g[2],g[3]]
         #存储路径需根据需要更改
        with open('str(goods)+'（'+str(depth*48)+'条数据）'+'.csv',"a+",encoding='GB18030',newline='') as csvfile:
        	w=csv.writer(csvfile)
        	w.writerow(out_putlist)
        	csvfile.close()
    	

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
