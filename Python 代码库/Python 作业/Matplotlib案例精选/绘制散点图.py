#绘制散点图

import numpy as np
import pylab as pl

a=np.arange(0,2.0*np.pi,0.1)
b=np.cos(a)
pl.scatter(a,b)
pl.show()
