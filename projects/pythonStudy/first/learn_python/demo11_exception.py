# coding:utf-8
# @SoftWare PyCharm
# @FileName demo11_exception.py
# @Auther zhanglin
# @Date 2021/05/19/0019 16:40
# @Describe python中的异常处理

print('---------try--except异常处理-------------')
try:
    a=10
    b=0
    result = a/b
    print('a/b结果为：',result)
except ZeroDivisionError:
    print('发生错误ZeroDivisionError，程序结束！')
except ValueError:
    print('发生错误ValueError，程序结束！')
print('----------------------------------------')
print('\n')

print('---------try--except--else异常处理-------------')
try:
    # a=int(input('请输入第一个数a：'))
    # b=int(input('请输入第二个数b：'))
    a=10
    b=2
    result = a/b
except Exception as e:
    print('发生错误，程序结束！')
else:
    print('a/b结果为：',result)
print('---------------------------------------------')
print('\n')

print('---------try--except--else--finally异常处理-------------')
try:
    # a=int(input('请输入第一个数a：'))
    # b=int(input('请输入第二个数b：'))
    a=10
    b=2
    result = a/b
except Exception as e:
    print('发生错误，程序结束！')
else:
    print('a/b结果为：',result)
finally:
    print('程序结束')
print('---------------------------------------------')
print('\n')

print('-------------python中的异常类型----------------')
print('除（或求余）零：ZeroDivisionError')
print('序列中没有次索引：IndexError')
print('映射中没有这个键：KeyError')
print('未声明/初始化对象（没有属性）:NameError')
print('语法错误:SyntaxError')
print('传入参数无效:ValueError')
print('---------------------------------------------')
print('\n')


print('-------------traceback打印异常----------------')
import traceback
try:
    c = 1/0
    print(c)
except:
    traceback.print_exc()
print('---------------------------------------------')
print('\n')
