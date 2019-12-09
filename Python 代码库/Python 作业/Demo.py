import random

Good_info=[{
            "title":"正版 从零开始学Python 数据分析与挖掘 python编程快速上手从入门到精通 语言程序设计基础教程书籍 零基础学python从入门到实战",
            "catelog_id":"1",
            "price":"39.50"
                },
           {
            "title":"2018最新款秋季帽衫",
            "catelog_id":"0",
            "url":"www.baidu1.com"
                },
           {
            "title":"2017最新款秋季帽衫",
            "catelog_id":"2",
            "url":"www.baidu2.com"
                }
           ]


for i in range(10):
    a=random.choice(Good_info)
    print(a["title"],a["catelog_id"],a["url"])


    

