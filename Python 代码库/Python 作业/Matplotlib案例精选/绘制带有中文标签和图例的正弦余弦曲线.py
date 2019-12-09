#绘制带有中文标签和图例的正弦余弦曲线

import numpy as np
import pylab as pl
from matplotlib import font_manager as fm

myfont=fm.FontProperties(fname=r'C:\Windows\Fonts\simkai.ttf')  #设置字体
t=np.arange(0.0,2.0*np.pi,0.01)                                  #自变量取值范围
s=np.sin(t)                                                      #计算正弦值
z=np.cos(t)                                                      #计算余弦值
pl.plot(t,s,label='正弦')
pl.plot(t,z,label='余弦')
pl.xlabel('x-variable',fontproperties='simkai',fontsize=24)         #设置x标签
pl.ylabel('y-sin_function_image',fontproperties='simkai',fontsize=24)
pl.title('sin-cos_function_image',fontproperties='simkai',fontsize=32)#图形的标题
pl.legend(prop=myfont)                                           #设置图例
pl.show()

'''本电脑中没有STKAITI所有没有支持中文标签的字体，先用英文代替，日后更换'''
