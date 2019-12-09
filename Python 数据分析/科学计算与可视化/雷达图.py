import matplotlib
import matplotlib.pyplot as plt 
import numpy as np
matplotlib.rcParams['font.family']='SimHei'           
matplotlib.rcParams['font.sans-serif']=['SimHei']   #为了正确显示中文字体，将字体更改为黑体‘SimHei’
data_labels=np.array(['工程师','实验员','艺术家','推销员','社会工作者','记事员'])
n=6
radar_labels=np.array(['    研究型(I)','艺术型(A)','社会型(S)',\
                     '企业型(E)   ','常规型(C)','现实型(R)'])    #  为了美观加了几个空格
data=np.array([[0.40,0.32,0.35,0.30,0.30,0.88],         #6种职业数据，列表元素为列表
              [0.85,0.35,0.30,0.40,0.40,0.30],
              [0.43,0.89,0.30,0.28,0.22,0.30],
              [0.30,0.25,0.48,0.85,0.45,0.40],
              [0.20,0.38,0.87,0.45,0.32,0.28],
              [0.34,0.31,0.38,0.40,0.92,0.28]]) 
angles=np.linspace(0,2*np.pi,n,endpoint=False)       #将360度平均分为n个部分（有endpoint=False分为6个部分，反之5个部分）
data=np.concatenate((data,[data[0]]))          
angles=np.concatenate((angles,[angles[0]]))        

plt.figure(facecolor='white')    #绘制全局绘图区域
plt.subplot(111,polar=True)    #绘制一个1行1列极坐标系子图，当前位置为1

plt.figtext(0.52,0.95,'霍兰德人格分析',ha='center',size=20)   #放置标题 ，ha是horizontalalignment（水平对齐方式）的缩写
plt.thetagrids(angles*180/np.pi,radar_labels)       #放置属性（radar_labels）
plt.plot(angles,data,'o-',linewidth=1.5,alpha=0.2)      #连线，画出不规则六边形
plt.fill(angles,data,alpha=0.25)        #填充，alpha是透明度（自己的实践理解）
legend=plt.legend(data_labels,loc=(0.94,0.80),labelspacing=0.1)    #放置图注（右上角）
plt.setp(legend.get_texts(),fontsize='small')      
plt.grid(True)    #打开坐标网格
plt.show()       #显示

