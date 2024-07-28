# coding:utf-8
# @SoftWare PyCharm
# @FileName demo09_str.py
# @Auther zhanglin
# @Date 2021/05/18/0018 11:28
# @Describe python中的字符串操作
import sys

print('----------------驻留机制-------------------')
# 字符串的驻留机制，内存中仅保存一份相同且不可变的字符串的方法
# 不同的值被存放在字符串的驻留内存池当中，对相同的字符串只保留一份copy
# 后续创建相同字符串时，不会开辟新的内存空间，而是把该字符串的地址赋给新变量
# 驻留机制的几种情况：
#   1、字符串长度为0或1时
#   2、符号标识符（字母、数字、下划线）的字符串 （不符合python标识符的字符串不驻留）
#   3、[-5,256]之间的整数数字
a = 'python'
b = 'python'
c = 'python'
print('a地址：', id(a))  # 2727070768432
print('b地址：', id(b))  # 2727070768432
print('c地址：', id(c))  # 2727070768432
print('\n')

a = -5
b = -5
print('[-5,256]之间的整数驻留：', a is b)
num1 = -1000
dnum2 = -1000
print('num1地址：', id(num1))
print('dnum2地址：', id(dnum2))
print('num1类型：', type(num1))
print('dnum2类型：', type(dnum2))
print('[-5,256]之外的整数不驻留：', num1 is dnum2)  # 正常应该为false,但pyCharm对驻留机制做了优化处理，使得原本不驻留的变量产生了驻留
print('\n')

print('字符串只在编译时进行驻留，而非运行时。')
print('字符串拼接建议使用join方法，而非+，因为join方法只创建一次对象，效率更高')
a = 'abc'
b = 'ab' + 'c'  # 运行之前完成连接（编译阶段），发生驻留。
c = ''.join(['ab', 'c'])  # 运行时连接 （运行阶段），会开辟新的存储空间。
print('a', id(a))  # 3140226246768
print('b', id(b))  # 3140226246768
print('c', id(c))  # 3140226329136
print('强制驻留前：', a is c)
c = sys.intern(a)  # 强制驻留
print('强制驻留后：', a is c)
print('-------------------------------------------')
print('\n')

print('----------------字符串查找-------------------')
a = 'abcdab'
print('index() 查找子串substr第一次出现的位置，找不到抛ValueError:', a.index('ab'))
print('rindex() 查找子串substr最后一次出现的位置，找不到抛ValueError:', a.rindex('ab'))
print('find() 查找子串substr第一次出现的位置，找不到返回-1:', a.find('ef'))
print('rfind() 查找子串substr最后一次出现的位置，找不到返回-1:', a.rfind('ef'))
print('-------------------------------------------')
print('\n')

print('----------------字符串转换-------------------')
a = 'hello WORLD'
print('upper() 转大写:', a.upper())  # 会产生一个新字符串对象
print('lower() 转小写:', a.lower())  # 会产生一个新字符串对象
print('swapcase() 将字符串中大写字符转小写，小写字符转大写:', a.swapcase())
print('capitalize() 将字符串中第一个字符转大写，其他转小写:', a.capitalize())
print('title() 将字符串中每个单词第一个字符转大写，其余转小写:', a.title())
print('-------------------------------------------')
print('\n')

print('----------------字符串对齐-------------------')
a = 'hello world'  # 长度11
print('center(宽度，填充符（可选，默认空格）) 居中对齐，如果设置宽度小于实际宽度泽返回原字符串:', a.center(21, '-'))
print('ljust(宽度，填充符（可选，默认空格）) 左对齐，如果设置宽度小于实际宽度泽返回原字符串:', a.ljust(21, '-'))
print('rjust(宽度，填充符（可选，默认空格）) 右对齐，如果设置宽度小于实际宽度泽返回原字符串:', a.rjust(21, '-'))
print('zfill(宽度) 右对齐，左边用0填充，如果设置宽度小于实际宽度泽返回原字符串:', a.zfill(21))
print('-------------------------------------------')
print('\n')

print('----------------字符串分割-------------------')
a = 'hello world python'
print('split分割，默认按空格分割：', a.split())
a = 'hello-world-python'
print('split分割，自定字符分割：', a.split('-'))
print('split分割，自定字符分割，指定最大分割次数：', a.split('-', 1))
a = 'hello world python'
print('rsplit分割，从字符串右侧开始分割，默认按空格分割：', a.rsplit())
a = 'hello-world-python'
print('rsplit分割，自定字符右分割，指定最大分割次数：', a.rsplit('-', 1))
print('-------------------------------------------')
print('\n')

print('----------------字符串判断-------------------')
a = 'helloworldpython'
print('isidentifier()，判断字符串是不是合法标识符：', a.isidentifier())
a = '''

    
'''
print('isspace()，判断字符串是否全由空白字符组成（回车、换行、水平制表符\\t）：', a.isspace())
a = 'acvfvfvf'
print('isalpha()，判断字符串是否全由字母组成：', a, a.isalpha())
a = '0b65654654'
print('isdecimal()，判断字符串是否全由十进制数组成：', a, a.isdecimal())
a = '0215465'
print('isnumeric()，判断字符串是否全由数字组成：', a, a.isnumeric())
a = 'asxax'
print('isalnum()，判断字符串是否全由字母和数字组成：', a, a.isalnum())
print('-------------------------------------------')
print('\n')

print('----------------字符串替换、合并-------------------')
a = 'helllo java java'
print('replace(被替换字串，替换字串，最大替换次数默最大) 替换：', a.replace('java', 'python'))
print('replace(被替换字串，替换字串，最大替换次数默最大) 替换：', a.replace('java', 'python', 1))
lst = ['a','b','c','d','e']
print('join() 把列表中的字符串合并成一个字符串：','|'.join(lst))
gt = ('a','b','c','d','e')
print('join() 把元组中的字符串合并成一个字符串：','|'.join(gt))
a = 'java'
print('join() 把字符串当作字符序列合并成一个字符串：','*'.join(a))
print('-------------------------------------------')
print('\n')

print('----------------字符串比较-------------------')
# > < <= >= != ==
# 比较规则：从头到尾挨个比较字符串中字符大小，相等时继续比较，不相等时停止比较后面字符，返回比较结果。
# 比较的是ordinal value(原始值)，调用内置函数ord可以得到指定字符ordinal value（Unicode）。
# 与内置函数ord对应的是内置函数chr,通过调用chr指定ordinal value可以得到与其对应的字符。
print('java原始值ord():',ord('j'))
print('python原始值ord():',ord('p'))
print('java>python:','java'>'python')
print('-------------------------------------------')
print('\n')

print('----------------字符串切片-------------------')
# 字符串是不可变序列，不具备增删改操作
# 切片操作将产生新的对象 str[start,end,step] start默认0，end默认最大，step默认1
a = 'hello python'
b = a[:5]
c = a[6:]
d = b + '!' + c
print('b',b,id(b))
print('c',c,id(c))
print('d',d,id(d))
print('-------------------------------------------')
print('\n')

print('----------------字符串格式化-------------------')
# 格式化字符串的两种方式
#   1、%作占位符 %s:字符串，%i或%d:整数，%f:浮点数  ‘我叫%s,今年%d岁。’ (name,age)
#   2、{}作占位符 ‘我叫{0}，今年{1}岁。’ format(name,age)
age = 18
name = '马奎斯'
hab = '摩托车'
print('我叫%s,今年%d岁。'%(name,age))
print('我叫{0},今年{1}岁,喜欢{2}'.format(name,age,'摩托车'))
print(f'我叫{name},今年{age}岁,喜欢{hab}') #python3特性

print('指定宽度:%10d' % 99) #指定宽度
print('指定精度:%.3f' % 3.141592653) #指定精度 （浮点数自动四舍五入）
print('指定精度显示三位数:{0:.3}'.format(3.141592653)) #指定精度
print('指定精度显示三位数:{:.3}'.format(3.141592653)) #指定精度
print('指定精度显示三位小数:{0:.3f}'.format(3.141592653)) #指定精度（浮点数自动四舍五入）
print('同时指定宽度和精度三位小数:{0:10.3f}'.format(3.141592653)) #同时指定宽度和精度（浮点数自动四舍五入）
print('同时指定宽度和精度显示三位小数:{:10.3f}'.format(3.141592653)) #同时指定宽度和精度（浮点数自动四舍五入）
print('同时指定宽度和精度:%10.3f' % 3.141592653) #同时指定宽度和精度
print('-------------------------------------------')
print('\n')

print('----------------字符串编码与解码-------------------')
# 编码：将字符串转换成二进制数据（bytes）
# 解码：将二进制数据（bytes）转换成字符串
a='张 python'
code = a.encode('GBK')
print('gbk编码：',code)
print('gbk解码:',code.decode('gbk'))
print('-------------------------------------------')
print('\n')

