
from faker import Faker
import random
from faker.providers import BaseProvider
fake = Faker('zh_CN')
class MyProvider(BaseProvider):
    def goods(self):
        goods=['数码产品','衣服','食品','书籍','床单被罩']
        return random.choice(goods)
fake.add_provider(MyProvider)
'''print('用户Peter今年的消费记录:')
for i in range(1,100):
    print("该用户在",fake.date_this_month(),"去了",
          fake.company(),"购买了",fake.goods(),sep='')'''

str = ""
for i in range(1,17):
    ch = chr(random.randrange(ord('0'), ord('9') + 1))
    str += ch
 
print(fake.uri() )
