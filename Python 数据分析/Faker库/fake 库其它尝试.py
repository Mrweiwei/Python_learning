from faker import Faker
import random
from faker.providers import BaseProvider

fake = Faker('zh_CN')

print(fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None))

print(fake.date_this_month(before_today=False, after_today=True))

print(fake.past_datetime(start_date="-30d", tzinfo=None))

print(fake.date_time_between(start_date="-90d", end_date="-59d"))
