#结巴分词的学习

import jieba

'''jieba.cut:该方法接收三个输入参数"
参数1：需要分词的字符串；
参数2：cut_all参数用来控制是否采用全模式，默认为精确模式；
cut_all=True 全模式
cur_all=False 精确（默认）模式
参数3：HMM参数用来控制是否适用HMM模型'''

seq_list1=jieba.cut("我来到北京清华大学",cut_all=True)
print("全模式："+"  ".join(seq_list1)) #全模式

seq_list2=jieba.cut("我来到北京清华大学",cut_all=False)
print("精确（默认）模式："+"  ".join(seq_list2))

seq_list3=jieba.cut("他来到了网易杭研大厦")  #默认是精确模式
print(",".join(seq_list3))

seq_list4=jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")
print("搜索引擎模式:"+",".join(seq_list4))
