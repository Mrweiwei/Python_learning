#爬取中国电竞价值排行榜—外设排行榜，利用cutecharts数据可视化分析

'''
爬取中国电竞价值排行榜-外设排行榜
网站：http://djws.uuu9.com/rank/201907/
数据类:键盘 鼠标 耳机 显示器 电竞椅 笔记本 显卡 路由器
数据项： 排名 型号厂家 天猫指数 京东指数 百度指数 性价指数 科技指数 综合指数
'''
import pandas as pd

url="http://djws.uuu9.com/rank/201907/"
url_read=pd.read_html(url,header=0)[0]#因为该网站数据存储在表格里，pandas的read_html函数可以快速的读取网页中的table的数据
url_read=url_read[url_read.index%2==0]
print(url_read)

'''def get_data(i):
    url="http://djws.uuu9.com/rank/20190%d/"%i
    url_read=pd.read_html(url,header=0)[0]
    url_read=url_read[url_read.index%2==0]
    return url_read'''

#df_data=[]
#df_data.append(get_data(3))
#循环抓取3-7月数据
#for i in range(3,8):
#    df_data.append(get_data(i))

#axis:1 表示列拼接，0 表示行拼接
#df=pd.concat(df_data,axis=0)
#print(df)
#df.to_csv(r'rich_list.csv',mode='a',encoding='utf_8_sig',header=0,index=False)





















