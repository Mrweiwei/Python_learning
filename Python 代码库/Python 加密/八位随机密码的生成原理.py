#八位随机密码生成算法的原理
import string
x=string.digits+string.ascii_letters+string.punctuation
import random
print("随机选取八个组合密码:")
print(''.join([random.choice(x)for i in range(8)]))
print("随机选取不重复的八个组合密码")
print(''.join(random.sample(x,8))
