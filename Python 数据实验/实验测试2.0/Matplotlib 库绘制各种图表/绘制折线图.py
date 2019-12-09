#折线图
'''绘制折线图，如果你数据不是很多的话，画出来的图将是曲折状态，但一旦你的数据集大起来，比如下面我们的示例，有100个点，所以我们用肉眼看到的将是一条平滑的曲线。

这里我绘制三条线，只要执行三次 plt.plot 就可以了。'''

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,2,100)
plt.plot(x,x,label="linear")
plt.plot(x,x**2,label="quadratic")
plt.plot(x,x**3,label="cubic")
plt.xlabel("x label")
plt.ylabel("y label")
plt.title("Simple Plot")
plt.legend()
#plt.show()
plt.savefig('折线图.png',bbox_inches='tight')
#第一个实参表示用什么样的文件名保存图片,第二个实参指定将图周围多余的空白剪裁掉
#如果不需要剪裁可以不写,文件保留在该.py文件目录处,看参数bbox这么好记的,却无所谓有无
