#词性标注
'''jieba.posseg.POSTokenizer(tokenizer=None)新建自定义分词，
tokenizer参数可指定内部使用的jieba.Tokenizer分词器。jieba
.posseg.dt为默认词性标注分词器。
标注句子分词后每个词的词性，采用ictclas兼容的标记法。'''

#官方历程
import jieba.posseg as pseg

words=pseg.cut("我爱学习蟒蛇")
#words类别为：generator


for word,flag in words:
    print('%s %s'%(word,flag))
