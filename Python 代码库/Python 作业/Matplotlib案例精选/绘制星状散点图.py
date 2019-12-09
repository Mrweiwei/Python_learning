#绘制星状散点图

import matplotlib.pylab as pl
import numpy as np
'''使用随机数生成数值，并根据数值大小来计算散点的大小'''
x=np.random.random(100)
y=np.random.random(100)
pl.scatter(x,y,s=x*500,c=u'r',marker=u'*')  #s指大小，c指颜色，marker指符号形状
pl.show()
