# coding:utf-8
# @SoftWare PyCharm
# @FileName demo07_tuple.py
# @Auther zhanglin
# @Date 2021/05/18/0018 9:58
# @Describe python中的元组

# 元组是python中的内置数据结构，是不可变序列
# 可变序列：列表、字典、集合 （可对序列执行增删改查操作，对象地址不会发送改变）
# 不可变序列：字符串、元组 （没有增删改查操作）

# 多任务环境下，同时操作可变序列对象时需要加锁。
# 因此，在程序中尽量使用不可变序列

# 元组创建方式
print('------------------元组创建-------------------------')
t1 = ('a', 'b', 'c', 'd', 'e')
print('元组创建结果t1:', t1)
print('元组数据类型t1：', type(t1))  # <class 'tuple'>
t2 = 'java', 'python', 'vue', 'c++', 98
print('元组创建结果t2:', t2)
print('元组数据类型t2：', type(t2))  # <class 'tuple'>
t3 = ('one',)  # 如果元组中只有一个元素，逗号不能少。
print('元组创建结果t3：', t3)
print('元组数据类型t3', type(t3))  # <class 'tuple'>
t4 = tuple((1, 2, 3, 4, 'e', 'f', 'g'))
print('元组创建结果t4：', t4)
print('元组数据类型t4', type(t4))  # <class 'tuple'>
t5 = ()
t6 = tuple()
print('空元组t5=()：', t5)
print('空元组t6=tuple()：', t6)
print('\n')

print('-----------------元组的遍历-----------------------')
t = tuple((1, 2, 3, 4, 'e', 'f', 'g'))
print('元组创建结果t：', t)
print('元组数据类型t', type(t))  # <class 'tuple'>
print('获取元组数据t[0]:', t[0])
print('获取元组数据t[1]:', t[1])
print('获取元组数据t[2]:', t[2])
print('获取元组数据t[3]:', t[3])
for item in t:
    print('遍历：', item, '类型：', type(item))
print('\n')
