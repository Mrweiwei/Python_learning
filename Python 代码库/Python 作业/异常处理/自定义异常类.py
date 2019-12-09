#如果需要，可以继承Python内置异常类来实现自定义的异常类

class ShortInputException(Exception):
    '''自定义异常类。'''
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length=length
        self.atleast=atleast
try:
    s=input('请输入-->')
    if len(s)<3:
        raise ShortInputException(len(s),3)
except EOFError:
    print('您输入了一个结束标记符EOF')
except ShortInputException as x:
    print('ShortInputException:输入的长度是%d,长度至少应是%d'%(x.length,x.atleast))
else:
    print('没有异常发生。')
