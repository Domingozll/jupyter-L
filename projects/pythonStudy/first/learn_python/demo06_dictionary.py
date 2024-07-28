# coding:utf-8
# @SoftWare PyCharm
# @FileName demo06_dictionary.py
# @Auther zhanglin
# @Date 2021/05/17/0017 18:12
# @Describe python中的字典

# 字典是python内置的一个数据结构，与列表一样是一个可变序列，以键值对的方式存储数据，字典是一个无序数列
print('---------字典创建-------------')
scores = {'张三': 18, '李四': 20, '王五': 35}
print('直接定义创建：', scores)
student = dict(name='jack', age=20)
print('dict函数创建创建：', student)
print('\n')

print('---------字典元素获取-------------')
scores = {'张三': 18, '李四': 20, '王五': 35}
print('字典元素获取：', scores['张三'])  # key不存在时抛KeyError
print('字典元素获取：', scores.get('王五'))  # Key不存在时返回None
print('Key不存在时返回指定值：', scores.get('麻七', 99))  # Key不存在时返回指定值
print('\n')

print('---------字典key的判断-------------')
print('字典key的判断:', '张三' in scores)
print('字典key的判断:', '张三' not in scores)
print('\n')

print('---------字典元素删除-------------')
del scores['张三']  # 删除指定键值对
print('删除后结果：', scores)
scores.clear()
print('字典元素清空后结果：', scores)
print('\n')

print('---------字典元素添加-------------')
scores = {'张三': 18, '李四': 20, '王五': 35}
scores['陈六'] = 99
print('添加后结果：', scores)
print('\n')

print('---------字典元素修改 -------------')
scores = {'张三': 18, '李四': 20, '王五': 35}
scores['张三'] = 10
print('修改后结果：', scores)
print('\n')

print('---------获取字典所有键、值 -------------')
keys = scores.keys()
print('字典所有键获取结果：', keys)
print('子弹见类型:', type(keys))  # <class 'dict_keys'>
print('字典keys视图转列表：', list(keys))
values = scores.values()
print('字典所有值获取结果：', values)
print('字典键类型:', type(values))  # <class 'dict_values'>
print('字典values视图转列表：', list(values))
items = scores.items()
print('获取字典所有键值对：', items)
print('字典键值items类型:', type(items))  # <class 'dict_items'>
print('字典键值对视图转列表：', list(items))
print('\n')

print('---------字典元素遍历 -------------')
for item in scores:
    print(item, scores[item], scores.get(item))
print('\n')

print('''
字典特点：
1、key不可重复，value可以重复
2、字典无序，存储顺序由key的hash值决定
3、字典会占用较大内存，但是查找速度很快。
''')
print('\n')

print('---------字典生成式 -------------')
items = ['a', 'b', 'c', 'd', 'e']
numbers = [1, 2, 3, 4, 5]
lst = zip(items, numbers)  # 以元素少的为基准
print('字典生成式1：', list(lst))
d = {item: number for item, number in zip(items, numbers)}
print('字典生成式2：', d)
