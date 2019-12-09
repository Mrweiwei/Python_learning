# 利用简单的python代码打印网站的各类信息 http://news.bitauto.com/xinchexiaoxi/20191002/1109800254.html
import urllib.request
#网址
url = "http://news.bitauto.com/xinchexiaoxi/20191002/1109800254.html"
#请求
request = urllib.request.Request(url)
#爬取结果
response = urllib.request.urlopen(request)
data = response.read()
#设置解码方式
data = data.decode('utf-8')
#打印结果
print(data)
#打印爬取网页的各类信息
print(type(response))
print(response.geturl())
print(response.info())
print(response.getcode())

