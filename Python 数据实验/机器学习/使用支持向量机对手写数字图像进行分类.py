'''使用支持向量机对手写数字图像进行分类
    首先生成大量图片并加入随机干扰，然后把这些图片划分为训练集和测试集，接下来使用训练集对模型进行训练，最后使用测试
    集进行评分。'''

from os import mkdir,listdir
from os.path import isdir,basename
from random import choice,randrange
from string import digits
from PIL import Image,ImageDraw
from PIL.ImageFont import truetype
from sklearn import svm
from sklearn.model_selection import train_test_split


#图像尺寸、图片中的数字字体大小、噪声比例
width,height=30,60
fontSize=40
noiseRate=8

def generateDigits(dstDir='datasets',num=40000):
    #生成num个包含数字的图片文件存放在当前目录下的datasets子目录
    if not isdir(dstDir):
        mkdir(dstDir)
    #digits.txt用来存储每个图片对应的数字
    with open(dstDir+'\\digits.txt','w') as fp:
        for i in range(num):
            #随机选择一个数字，生成对应的彩色图像文件
            digit=choice(digits)
            im=Image.new('RGB',(width,height),(255,255,255))
            imDraw=ImageDraw.Draw(im)
            font=truetype('c:\\windows\\fonts\\TIMESBD.TTF',fontSize)
            #写入黑色字体
            imDraw.text((0,0),digit,font=font,fill=(0,0,0))
            #加入随机干扰
            for j in range(int(noiseRate*width*height)):
                w,h=randrange(1,width-1),randrange(height)
                #水平交换两个相邻像素的颜色
                c1=im.getpixel((w,h))
                c2=im.getpixel((w+1,h))
                imDraw.point((w,h),fill=c2)
                imDraw.point((w+1,h),fill=c1)
            im.save(dstDir+'\\'+str(i)+'.jpg')
            fp.write(digit+'\n')

def loadDigits(dstDir='datasets'):
    #获取所有图像文件名
    digitsFile=[dstDir+'\\'+fn for fn in listdir(dstDir) if fn.endswith('.jpg')]
    #按编号排序
    digitsFile.sort(key=lambda fn:int(basename(fn)[:-4]))
    #digitsData用于存放读取的图片中数字信息
    #每个图片中所有像素值存放于digitsData中的一行数据
    digitsData=[]
    for fn in digitsFile:
        with Image.open(fn) as im:
            # getpixel()方法用来读取指定位置像素的颜色值
            data=[sum(im.getpixel((w,h)))/len(im.getpixel((w,h))) for w in range(width) for h in range(height)]
            digitsData.append(data)
    #digitsLabel用于存放图片中的数字的标准分类
    with open(dstDir+'\\digits.txt') as fp:
        digitsLabel=fp.readlines()
    #删除数字字符两侧的空白字符
    digitsLabel=[label.strip() for label in digitsLabel]
    return (digitsData,digitsLabel)

#生成图片文件
generateDigits(num=100)
#加载数据
data=loadDigits()

print('数据加载完成。')

#随机划分训练集合测试集，其中参数test_size用来指定测试集大小
X_train,X_test,y_train,y_test=train_test_split(data[0],data[1],test_size=0.1)

#创建并训练模型
svcClassifier=svm.SVC(kernel="linear",C=1000,gamma=0.001)
svcClassifier.fit(X_train,y_train)
print('模型训练完成。')

#使用测试集对模型进行评分
score=svcClassifier.score(X_test,y_test)
print("模型测试得分：",score)


















































    

















            
            


























    
