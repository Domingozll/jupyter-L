# coding:utf-8
# @Auther zhanglin
# @Date 2021/05/14/0014 16:35
# @Describe python学习笔记

# 变量
name = '张琳'
print('值', name)
print('内存地址', id(name))
print('类型', type(name))
print('\n')

# 数据类型
# int 整型
print('十进制', 118)
print('二进制', 0b1011011)  # 加 0b
print('八进制', 0o156)  # 加 0o
print('十六进制', 0xEAF)  # 加 0x
print('\n')
# float 浮点型
f1 = 1.1
f2 = 2.2
print('浮点数计算误差1：', f1 + f2)  # 3.3000000000000003
from decimal import Decimal

print('浮点数计算误差2：', Decimal(f1) + Decimal(f2))  # 3.300000000000000266453525910
print('浮点数计算误差3：', Decimal(1.1) + Decimal(2.2))  # 3.300000000000000266453525910
print('消除计算误差：', Decimal('1.1') + Decimal('2.2'))  # 3.3
print('\n')
# bool 布尔型
print('布尔false', False)  # 1
print('布尔true', True)  # 1
print('布尔转整数True+1', True + 1)  # 2
print('布尔转整数False+1', False + 1)  # 1
print('\n')
# str 字符串
str1 = 'python天下第一，' \
       'java天下第二'
str2 = "python天下第一，" \
       "java天下第二"
str3 = """python天下第一，
java天下第二"""
str4 = '''python天下第一，
java天下第二'''
print('单引号\'\'', str1)
print('双引号\"\"', str2)
print('三个双引号\"\"\"   \"\"\"\"(可以打印换行)', str3)
print('三个单引号\'\'\'   \'\'\'\'(可以打印换行)', str4)
print('\n')

# 数据类型转换
name = '张三'
age = 18
# print('数据转换：',name+age) # 报错
print('数据转换str()：', '我叫' + name + '，今年' + str(age) + '岁')  # int转str
print('\n')
s1 = '128'
s2 = 12.5
s3 = True
s4 = '12.5'  # 不可转
s5 = 'name'  # 不可转
print('数据转换int(\'128\') 字符串：', int(s1))  # 字符串
print('数据转换int(12.5) 浮点型：', int(s2))  # 浮点型
print('数据转换int(True) 布尔型：', int(s3))  # 布尔型
# print('数据转换int(\'12.5\') 字符串：', int(s4))  # 字符串 报错
# print('数据转换int('name') 字符串：', int(s4))  # 字符串 报错
print('\n')
# print('数据转换float()：', '我叫' + name + '，今年' + str(age) + '岁')  # int转str
print('数据转换flaot(123)', float(123))
print('数据转换flaot(123.2)', float(123.2))
print('数据转换flaot(\'123.2\')', float('123.2'))
print('数据转换flaot(True)', float(True))
print('\n')
# print('数据转换flaot(aaa)',float('aaa')) #报错


# 单行注释
'''
多行注释
多行注释
多行注释
多行注释
'''
"""
多行注释
多行注释
多行注释
多行注释
"""
# 中文编码 默认utf-8 须在代码第一行声明
# coding:gbk
# coding:utf-8
