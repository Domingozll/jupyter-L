# coding:utf-8
# @SoftWare PyCharm
# @FileName demo02.py
# @Auther zhanglin
# @Date 2021/05/20/0020 11:38
# @Describe 动态绑定属性和方法

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '在吃饭')


stu1 = Student('张三', 20)
stu2 = Student('李四', 18)

print('-----------动态绑定属性---------------')
print(stu1.name, stu1.age)
print(stu2.name, stu2.age)
print('-----------动态绑定属性--end----------')
print('\n')

print('-----------动态绑定方法---------------')


def show():
    print('动态方法show()')


stu1.show = show
stu1.show()
print('-----------动态绑定方法--end----------')
print('\n')

print('-----------python中的私有属性---------------')


class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 属性加__表示私有属性，只能在类内部使用，不可被实例对象直接使用。

    def show(self):
        print(self.name, self.__age)


stu1 = Student('张三', 20)
print(stu1.name)
stu1.show()
# print(stu1.__age) #报错,私有属性不可在类外部使用
print('类的外部使用私有属性：', stu1._Student__age)  # 可以通过——Student——
print('查看实例对象中的所有属性和方法：\n', dir(stu1))
print('-----------python中的私有属性--end----------')
print('\n')

print('-----------python中的继承-------------')


# 默认继承object 同java
class Person(object):  # object可以省略
    def __init__(self, age, name):
        self.__age = age
        self.__name = name

    def info(self):
        print('姓名：', self.__name, '年龄：', self.__age)


per = Person(18, '张三')
per.info()


class Student(Person):
    def __init__(self, age, name, level):
        self.__level = level
        super(Student, self).__init__(age, name)

    def info(self):
        super().info()
        print('班级：', self.__level)


stu = Student(18, '李四', '三年级')
stu.info()

# 多继承
print('python中的多继承：')


class A(object):
    print('我是A')


class B(A):
    print('我是B')


class C(A):
    print('我是C')


class D(B, C):
    print('我是D')


d = D
print('-----------python中的继承--end--------')
print('\n')

print('-----------python中的多态-------------')


class Animal(object):
    def eat(self):
        print('动物吃东西')


class Dog(Animal):
    def eat(self):
        print('狗吃骨头')


class Cat(Animal):
    def eat(self):
        print('猫吃鱼')


class Person(object):
    def eat(self):
        print('人吃饭')


def fun(obj):
    obj.eat()


p = Person()
fun(p)
# python是动态语言，只关心对象的行为，不关心对象的类型。可以在创建对象后动态的绑定属性和方法。
# java是静态语言，静态语言实现多态的三个必要条件：
# 1、继承
# 2、方法重写
# 3、父类引用指向子类对象
print('-----------python中的多态--end--------')
print('\n')

print('-----------python中的特殊属性-------------')


# 特殊属性：
# __dict__获得对象或实例所绑定的所有属性和方法的字典
# ………………等等
class A:
    def __init__(self, age):
        self.age = age


class B:
    def __init__(self, name):
        self.name = name


class C(A, B):
    def __init__(self, gender):
        self.gender = gender


c = C('男')
print('实例对象的属性字典:', c.__dict__)  # {'gender': '男'}
print('类对象的属性字典:',
      C.__dict__)  # {'__module__': '__main__', '__init__': <function C.__init__ at 0x000002080391CC10>, '__doc__': None}
print('实例对象的类型:', c.__class__)  # <class '__main__.C'> 输出对象所属的类
print('类对象的类型:', C.__class__)  # <class 'type'>
print('第一个父类类型的元素(基类):', C.__base__)  # <class '__main__.A'>
print('所有父类类型的元素:', C.__bases__)  # (<class '__main__.A'>, <class '__main__.B'>)
print('类的层次结构:', C.__mro__)  # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
print('类的子类:', A.__subclasses__())  # [<class '__main__.C'>]
print('-----------python中的特殊属性--end--------')
print('\n')

print('-----------python中的特殊方法-------------')
# 特殊方法：
# __len__()通过重写—__len__()方法，让内置函数len()的参数可以是自定义类型
# __add__()通过重写—__add__()方法，可使自定义对象具有“+”功能
# __new__()用于创建对象
# __init__()对创建的对象进行初始化
a = 20
b = 10
c = a + b
d = a.__add__(b)
print('c：',c,'d：',d)
print('__len__()方法：')
class Student:
    def __init__(self,name):
        self.name = name
    def __add__(self, other):
        return self.name + other.name
    def __len__(self):
        return 18
s1 = Student('张三')
s2 = Student('李四')
print('重新__add__()实现两个对象的加法运算：',s1+s2)
print('__len__()方法：')
lst = [1,2,3,4,5]
str = 'aaaa'
print(len(lst))
print(len(str))
print(len(s1))

class Person:
    def __init__(self,name,age):
        print('__init__被调用了，self的id值为：{0}'.format(id(self)))
        self.name = name
        self.age = age
    def __new__(cls, *args, **kwargs): #先于__init__方法执行
        print('__new__被调用了，cls的id值为：{0}'.format(id(cls)))
        obj = super().__new__(cls)
        print('__new__方法中创建的对象id值为：{0}'.format(id(obj)))
        return obj
print('object这个类对象的id值为：{0}'.format(id(object)))
print('Person这个类对象的id值为：{0}'.format(id(Person)))
p1 = Person('张三',18) #调用Person中__new__()方法
print('p1这个对象的id值为：{0}'.format(id(p1)))

print('-----------python中的特殊方法--end--------')
print('\n')
