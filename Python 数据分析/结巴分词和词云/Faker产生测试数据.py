#from faker import Factory
from faker import Faker
import random

#faker=Factory.create()
#print(faker)

'''print('Peter 账户的账单如下:')
for i in range(1,100):
    print(fake.date_this_month(),\
          fake.company_prefix(),fake.job())
'''


fake=Faker(locale="zh_CN")
'''with open("log.txt","w")as f:
    f.write(str(fake.profile()))'''
        
print('用户Peter今年的消费记录:')
for i in range(1,10):
    print(fake.currency_code())
    '''print("该用户在",fake.date_this_month,"去了",
          fake.company(),"购买了",fake.goods())'''





















    
    
