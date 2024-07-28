# coding:utf-8
# @SoftWare PyCharm
# @FileName demo02_basic02.py
# @Auther zhanglin
# @Date 2021/05/14/0014 18:06
# @Describe python函数

# 输入函数 input
# present = input('我是你爸爸')
# print(present)
# print('over!\n')
# a=input('a=')
# b=input('b=')
# print(type(a),type(b))
# print(a+b)
# b=int(b)
# a=int(a)
# print(type(a),type(b))

# a=int(input('a='))
# b=int(input('b='))
# print(type(a),type(b))
# print(a+b)

# 算数运算
print('加法运输1+1=', 1 + 1)  # 加法运输
print('减法运输1-1=', 1 - 1)  # 减法运输
print('乘法运输2*4=', 2 * 4)  # 乘法运输
print('除法运输11/2=', 11 / 2)  # 除法运输
print('整除运算（两个正数）9//4=', 9 // 4)  # 整除运算 两个正数
print('整除运算（两个负数）-9//-4=', -9 // -4)  # 整除运算 两个负数
print('整除运算（一正一负，向下取整）9//-4=', 9 // -4)  # 整除运算 一正一负，向下取整 -2.2取-3
print('整除运算（一正一负，向下取整）-9//4=', -9 // 4)  # 整除运算 一正一负，向下取整 -2.2取-3
print('取余运算 一正一负：-3=9-（-4）*（-3）、、、9%-4=', 9 % -4)  # 求余运算 一正一负：余数=被除数-除数*商
print('取余运算 一正一负：3=-9-4*（-3）、、、-9%4=', -9 % 4)  # 求余运算 一正一负：余数=被除数-除数*商
print('幂运算2**2=', 2 ** 2)  # 幂运算
print('\n')

# 赋值运算
a = 3 + 4
print('a=3+4', a)
# 链式赋值
a = b = c = 4
print('链式赋值a=b=c=4： a=', a, '内存地址：', id(a))
print('链式赋值a=b=c=4： b=', b, '内存地址：', id(b))
print('链式赋值a=b=c=4： c=', c, '内存地址：', id(c))
print('\n')
# 参数赋值
a = 20
a += 30
print('+=', a)
a = 20
a -= 30
print('-=', a)
a = 20
a *= 30
print('*=', a)
a = 20
a /= 30
print('/=', a)
a = 20
a //= 30
print('//=', a)
a = 20
a %= 30
print('%=', a)
print(20 % 30)
print(30 % 20)
# 系列解包赋值
a, b, c = 10, 20, 30
print('系列解包赋值a,b,c=10,20,30： a=', a, '内存地址：', id(a))
print('系列解包赋值a,b,c=10,20,30： b=', b, '内存地址：', id(b))
print('系列解包赋值a,b,c=10,20,30： c=', c, '内存地址：', id(c))
print('\n')

# 比较运算
a, b = 10, 20
print('10>20:', a > b)
print('10<20:', a < b)
print('10==20:', a == b)
print('10!=20:', a != b)
print('10>=20:', a >= b)
print('10<=20:', a <= b)
a, b = 10, 10
print('a is b:', a is b)  # 比较内存地址 a与b值相等时，不在创建新的存储空间
print('a is not b:', a is not b)  # 比较内存地址 a与b值相等时，不在创建新的存储空间
a, b = 10, 20
print('a is b:', a is b)  # 比较内存地址 a与b值不相等时，创建新的存储空间
print('a is not b:', a is not b)  # 比较内存地址 a与b值相等时，不在创建新的存储空间

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print('list1 is list2:', list1 is list2)  # 比较内存地址 数组值一样时，也会开辟新内存空间
print('list1 is not list2:', list1 is not list2)  # 比较内存地址 数组值一样时，也会开辟新内存空间
print('list1==list2:', list1 == list2)  # 比较值

# 布尔运算
# and ==>java中 &&
# or  ==>java中 ||
# not ==>java中 !
# in ==> java中没有
# not in ==> java中没有
s = 'hello'
print('h' in s)
print('w' in s)
print('h' not in s)
print('w' not in s)

# 位运算
print('与运算4&8：', 4 & 8)  # 4二进制数：00000100 8二进制数：00001000 二进制按位与 结果为00000000十进制0
print('或运算4|8：', 4 | 8)  # 4二进制数：00000100 8二进制数：00001000 二进制按位或 结果为00001100十进制12
print('左移位运算（高位溢出，低位补0，十进制数乘以2*1）', 4 << 1)
print('右移位运算（低位一处，高位补0，十进制数除以2*2）', 4 >> 2)

# 运算优先级
# [ 括号 () ] > [算数运算 幂运算>乘除求余>加减] > [位运算 (<<,>>) > & >| ] > [比较运算 >,<,>=,<=,==,!=] > [布尔运算 and>or ] > [赋值运算 = ]
