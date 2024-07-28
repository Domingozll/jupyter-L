# coding:utf-8
# @SoftWare PyCharm
# @FileName demo08_set.py
# @Auther zhanglin
# @Date 2021/05/18/0018 10:22
# @Describe python中的集合

# 集合是python内置数据结构，可变序列，是没有value的字典
# hash函数
a = 's111'
b = 's222'
print('hash值a：', hash(a))
print('hash值b：', hash(b))

print('-------------集合的创建-----------------')
s1 = {1, 2, 3, 4, 2, 2, 'c'}  # 集合元素不可重复，如果重复会自动去重。
print('集合创建s1:', s1)
print('集合类型s1：', type(s1))  # <class 'set'>
s2 = set((range(6)))
print('集合创建s2:', s2)
print('集合类型s2：', type(s2))  # <class 'set'>
s3 = set((1, 2, 3, 4))
print('集合创建s3,元组转集合:', s3)
print('集合类型s3：', type(s3))  # <class 'set'>
s4 = set(('python'))
print('集合创建s4,字符串转集合:', s4)
print('集合类型s4：', type(s4))  # <class 'set'>
s5 = {}  # 创建的是空字典，不是空集合
s6 = set()
print('空集合s5={}（错误演示）:', type(s5))  # <class 'dict'>
print('空集合s6=set():', type(s6))  # <class 'set'>
print('\n')

print('-----------------集合的相关操作-------------------------')
s = {1, 2, 3, 4, 5, 6, 7, 8}
print('集合元素的判断01：', 1 in s)
print('集合元素的判断02：', 1 not in s)
s.add(80)
print('集合元素的新增add()，一次添加一个元素：', s)
s.update({200, 300, 400})
print('集合元素的新增update()，添加集合：', s)
s.update(('a', 'b', 'c'))
print('集合元素的新增update()，添加元组：', s)
s.remove(200)
print('一次删除一个指定元素,元素不存在是抛异常 remove()：', s)
s.discard(300)
print('一次删除一个指定元素，元素不存在时不抛异常 discard()：', s)
s.pop()
print('一次删除一个任意元素 pop()：', s)
s.clear()
print('清空集合 clear()：', s)
print('\n')

print('------------------集合间的关系---------------------------')
s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3}
print('两个集合是否相等 == ：', s1 == s2)
print('两个集合是否不相等 != ：', s1 != s2)
print('一个集合是否另一个集合的子集 issubset：', s2.issubset(s1))
print('一个集合是否另一个集合的超集 issuperset：', s1.issuperset(s2))
print('两个集合是否没有交集 isdisjoint：', s1.isdisjoint(s2))
print('\n')

print('------------------集合的数学操作---------------------------')
s1 = {1, 2, 3, 4, 5, 7, 9}
s2 = {1, 3, 5, 6, 8}
s3 = s1.intersection(s2)
print('交集intersection：', s3)
s3 = s1.union(s2)
print('并集union：', s3)
s3 = s1 | s2
print('并集 | ：', s3)
s3 = s1.difference(s2)
print('差集difference：', s3)
s3 = s2.difference(s1)
print('差集difference：', s3)
s3 = s1 - s2
print('差集 - ：', s3)
s3 = s1.symmetric_difference(s2)
print('对称差集symmetric_difference：', s3)
s3 = s2.symmetric_difference(s1)
print('对称差集symmetric_difference：', s3)
s3 = s1 ^ s2
print('对称差集 ^ ：', s3)
print('\n')

print('------------------集合生成式---------------------------')
s = {i * i for i in range(8)}
print('集合生成结果：', s)
print('生成类似：', type(s))
