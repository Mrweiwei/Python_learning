#散点图
'''其实散点图和折线图是一样的原理，将散点图里的点用线连接起来就是折线图了。所以绘制散点图，只要设置一下线型即可。

注意：这里我也绘制三条线，和上面不同的是，我只用一个 plt.plot 就可以了。'''

import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0., 5., 0.2)
# 红色破折号, 蓝色方块 ，绿色三角块
plt.plot(x, x, 'r--', x, x**2, 'bs', x, x**3, 'g^')
plt.show()
