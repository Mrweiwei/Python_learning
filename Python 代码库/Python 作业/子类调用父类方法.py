#在派生类中调用基类的方法

class Person(object):     #必须以object为基类
    '''首先设计Person类，然后以Person为基类派生Teacher类，分别创建Person类和Teacher类的对象，并在派生类中调用基类方法'''
    def __init__(self,name='',age=24,sex='man'):
        self.setName(name)
        self.setAge(age)
        self.setSex(sex)

    def setName(self,name):
        if not isinstance(name,str):
            print('name must be string.')
            return
        self.__name=name

    def setAge(self,age):
        if not isinstance(age,int):
            print('age must be integer.')
            return
        self.__age=age

    def setSex(self,sex):
        if sex !='man' and sex !='woman':
            print('sex must be "man" or "woman"')
            return
        self.__sex=sex

    def show(self):
        print('Name:',self.__name)#注意是私有属性
        print('Age:',self.__age)
        print('Sex:',self.__sex)

class Teacher(Person):
    def __init__(self,name='',age=30,sex='man',department='Computer'):
        super(Teacher,self).__init__(name,age,sex)
        ##or,use another method like below:
        #Person.__init__(self,name,age,sex)
        self.setDepartment(department)


    def setDepartment(self,department):
        if not isinstance(department,str):
            print('department must be string')
            return
        self.__department=department

    def show(self):
        super(Teacher,self).show()
        print('Department',self.__department)

if __name__=='__main__':
    zhangsan=Person('Zhangsan',19,'man')
    zhangsan.show()
    lisi=Teacher('Lisi',32,'man','Math')
    lisi.show()
    lisi.setAge(40)
    lisi.show()











    



















            



        
    
