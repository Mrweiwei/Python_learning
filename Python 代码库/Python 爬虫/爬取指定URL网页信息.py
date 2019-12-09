#爬取指定URL的网页信息

import requests    #导入requests模块（获取网页）
r=requests.get('http://www.amazon.cn')  #获取指定URL的网页信息
import re
pa=re.compile(r'<option.+>(.+?)</option>')
option=pa.findall(r.text)
for get_text in option:
    print(get_text)
