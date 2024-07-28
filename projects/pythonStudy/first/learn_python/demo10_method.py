# coding:utf-8
# @SoftWare PyCharm
# @FileName demo10_method.py
# @Auther zhanglin
# @Date 2021/05/19/0019 9:43
# @Describe python中的函数

print('--------------函数的创建和调用----------------')
'''
def 函数名 ([输入参数]):
    函数体
    [return xxx]
'''


def calc(a, b):
    c = a + b
    return a


print('函数demo01:', calc(1, 2))
print('函数demo02,关键字传参:', calc(b=1, a=2))


def m1(a, b):
    a = 100
    b.append(10)
    return


a = 10
b = [1, 1, 1, 1, 1]
print('python引用传递演示：')
print('调用之前a:', a, id(a))
print('调用之前b:', b, id(b))
m1(a, b)
print('调用之后a:', a, id(a))
print('调用之后b:', b, id(b))
print('-------------------------------------------')
print('\n')

print('-----------------函数的返回------------------')
print('函数返回多个值时，结果为元组：')


def fun(num):
    odd = []  # 存奇数
    even = []  # 存偶数
    for i in num:
        if i % 2:  # 零的布尔值为True
            odd.append(i)
        else:  # 非零整数布尔值为True
            even.append(i)
    return odd, even


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print('函数的返回:', fun(lst))  # 可以传列表，返回元组 ([1, 3, 5, 7, 9, 11], [2, 4, 6, 8, 10, 12])
print('-------------------------------------------')
print('\n')

print('---------------函数的参数定义----------------')


def fun(*a):
    return a


print('函数默认值参数：', fun(10), end='\t')
print('函数默认值参数：', fun(10, 20))


def fun(a, b=10):
    return a + b


print('函数默认值参数：', fun(10), end='\t')
print('函数默认值参数：', fun(10, 20))


def fun(*a):
    print('个数可变的位置参数(传递元组)：', a)


fun(10, 20)
fun(10, 20, 30, 40)


def fun(**a):
    print('个数可变的关键字形参（传递字典）：', a)


fun(a=10, b=20)
fun(a=10, b=20, c=30, d=40)
'''
def fun(**a):
    print(a)
def fun(*a):
    print(a)
以上代码会报错，个数可变的位置参数及关键字形参只能是一个
'''


def fun(*a, **b):
    pass


'''
def fun(*a,**b):
    pass
会报错。在既有个数可变的关键字形参和个数可变的位置参数时
要求个数可变的位置参数放在前面 
'''


def fun(a, b, c):
    print('a:', a)
    print('b:', b)
    print('c:', c)
    return ''


dic = {'a': 1, 'b': 2, 'c': 3}
print('字典传参：', fun(**dic))  # 将字典中的键值对转换为关键字实参传入
tup = ([1, 1], (2, 2), {'c': 3})
print('元组传参：', fun(*tup))
lst = [1, 2, 3]
print('列表传参：', fun(*lst))


def fun(a, b, *, c, d):  # 从*后的参数 c、d 只能采用关键字形参传入
    print('传参结果：', a, b, c, d)


'''
报错：
def fun(a,b,*,*c,**d):
    pass
'''


def fun(a, b, *c, **d):
    pass


fun(10, 20, c=30, d=40)
print('错误定义：fun(a,b,*,**d)')
'''
报错：
def fun(a,b,*,**d):
    pass
'''


def fun(a, b, *, c, **d):
    pass


print('错误定义：fun(a,b,*,c,*d)')
'''
def fun(a,b,*,c,*d):
    pass
'''
print('-------------------python中的变量作用域------------------------')
name = '张三'  # 函数内部外部都可以使用
def fun():
    global age  # 将局部变量声明为全局变量
    age = 100  # 仅在函数内部可以使用
    global name
    print('方法内使用全局变量：', name)
    name = '李四'
    print('方法内声明全局变量：', age)

fun()
print('全局变量:', name)
print('方法外使用方法内声明的全局变量:', age)
print('\n')
