# coding:utf-8
# @SoftWare PyCharm
# @FileName demo01_class.py
# @Auther zhanglin
# @Date 2021/05/20/0020 11:10
# @Describe python中的类
print('-------------------类的声明-------------------------')
class Student: #命名规则同java
    loction = '北京'  # 直接写在类里的变量，叫做类属性
    def __init__(self,age,name): #定义在类之内的叫方法，必须加参数(self)。定义在类以外的称为函数
        self.age = age # self.age 称为实例属性
        self.name = name
        print('创建类：name=',name,'age=',age)

    #实例方法
    def fun1(self):
        print('我是实例方法')

    #静态方法
    @staticmethod
    def fun2():
        print('我是静态方法，用@staticmethod修饰')

    #类方法
    @classmethod
    def fun3(cls): #调用的时候不需要传入
        print('我是类方法，用@classmethod修饰')

print(id(Student)) #2455491957344 类对象地址
print(type(Student)) #<class 'type'>
print(Student) #<class '__main__.Student'>
print('-------------------类的声明--end-------------------------')
print('\n')


print('-------------------对象的创建-------------------------')
stu = Student(18,'张三')
print(id(stu)) #1712324411344 实例对象地址
print(type(stu)) #<class '__main__.Student'>
print(stu) #默认调用__str__()方法  <__main__.Student object at 0x0000018EAE7CFFD0> 0x0000018EAE7CFFD0为内存地址1712324411344的十六进制
print(stu.loction)
stu.fun1()
Student.fun1(stu)

stu.fun2()
Student.fun2()

stu.fun3()
Student.fun3()
stu2 = Student(20,'李四')
print(stu2.loction)
print('-------------------对象的创建--end--------------------')
print('\n')