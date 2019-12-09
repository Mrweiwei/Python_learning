#使用扩展库schedule实现更强大的任务调用功能
import time
import schedule

def myJob1():
    print('Job1:我30秒执行一次，每次执行3秒')
    time.sleep(3)
schedule.every(30).seconds.do(myJob1)

def myJob2():
    print('Job2:我一分钟执行一次，每次执行5秒')
    time.sleep(5)
schedule.every(1).minutes.do(myJob2)

def myJob3():
    print('Job3:我每天下午15:20执行一次，每次执行5秒')
    time.sleep(5)
schedule.every().day.at('15:20').do(myJob3)

def myJob4():
    print('Job4:我每隔5到10秒（具体时间随机）执行一次，每次执行3秒')
    time.sleep(3)
schedule.every(5).to (10).seconds.do(myJob4)

def myJob5():
    print('Job5:我每周日下午15:21执行一次，每次执行3秒')
    time.sleep(3)
schedule.every().sunday.at('15:21').do(myJob5)

while(True):
    schedule.run_peding()
