# coding:utf-8
# @SoftWare PyCharm
# @FileName demo04_if_while_for.py
# @Auther zhanglin
# @Date 2021/05/14/0014 19:36
# @Describe python分支结构

# if else
a = 100
b = 10
if a > b:
    print(True)
else:
    print(False)
print('\n')

# if elif [else:] 多分支结构
if 1 > 1:
    print('1')
elif 2 < 3:
    print('2')
elif 3 > 3:
    print('3')
else:
    print('4')
print('\n')

# 条件表达式
print('条件表达式', ('1') if 1 > 2 else ('2'))
print('\n')

# pass语句
print('----------pass语句--------------')
if 1 > 2:
    pass
else:
    print(1)
print('\n')

# range函数
r = range(10)
print('range函数 range(stop)：', list(r))
r = range(10, 20)
print('range函数 range(10,20)：', list(r))
r = range(10, 50, 10)
print('range函数 range(10,50,10)：', list(r))

# in / not in
print(1 in r)
print(1 not in r)

# 循环结构
print('-------------while循环结构-----------------')
a = 1
while a < 10:
    print('while循环1', a)
    a += 1
print('\n')
print('-------------for循环结构-----------------')
for item in 'Python':
    print('for:', item)

print('-------------for循环结构：break、continue、for-……-else-----------------')
for i in range(10):
    if i == 100:
        print('i:', i)
        break
    else:
        continue
else:
    print('for结束')  # 循环正常结束时执行，break或异常时不执行
