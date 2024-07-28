# coding:utf-8
# @SoftWare PyCharm
# @FileName demo05_list.py
# @Auther zhanglin
# @Date 2021/05/17/0017 16:04
# @Describe python中的list 列表

a = 10
str = 'sss'
b = 10.2

lst = [a, str, b]
lst2 = list([a, str, b])
print('sss' in lst)
print('sss' in lst2)
print('lst[0]:', lst2[0])
print('lst2[-2]:', lst2[-2])
print('type(lst):', type(lst))
print('lst.index()', lst.index(10.2))
print('lst.index()', lst.index(10.2, 1, 100))
lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print('------list切片 lst[start,stop,step]------')
print('原列表lst:', lst)
print('lst[1:6]:', lst[1:6])
print('lst[1:6:]:', lst[1:6:])
print('lst[1:6:1]:', lst[1:6:1])
print('lst[2:6:2]:', lst[2:6:2])
print('lst[:7:2]:', lst[:7:2])
print('lst[2::2]:', lst[2::2])
print('lst[::2]:', lst[::2])
print('lst[3::]:', lst[3::])
print('lst[::]:', lst[::])
print('原列表id：', id(lst))
print('切片列表id：', id(lst[1:6]))  # 新切出列表为新列表
print('------list切片 step为负数------')
print('原列表lst:', lst)
print('lst[::-1]:', lst[::-1])  # step为负数时，从后往前数。start默认为-size
print('lst[9:-11:-1]:', lst[9:-11:-1])  # step为负数时，从后往前数。start默认为-size
print('lst[2::-1]:', lst[2::-1])
print('lst[2::-1]:', lst[2::-1])
print('lst[2:9:-1]:', lst[2:9:-1])
print('lst[2:-10:-1]:', lst[2:-10:-1])
print('\n')

print('------list.append()元素添加------')
print('添加前lst:', lst)
print('添加前id(lst):', id(lst))
lst.append(1000)
print('添加后id(lst):', id(lst))  # 地址不变
print('添加后lst:', lst)
print('\n')

print('------list.extend()元素扩展------')
lst2 = [1, 2, 3]
lst.append(lst2)  # 将lst2作为一个数组添加到lst结尾
print(lst)
lst.extend(lst2)  # 向列表一次添加多个元素
print('lst.extend(lst2)后:', lst)
print('\n')

print('------list.insert()元素插入------')
lst = [0, 1, 2, 3, 4]
c = lst.insert(6, 90)  # 返回None
print(lst[5])
print('c', c)
print('lst插入后结果：', lst)
print('\n')

print('------list切片批量替换元素------')
lst2 = ['a', 'b', 'c', 'd', 'e', 'f']
lst[1::] = lst2
print('lst切片批量替换后结果：', lst)
print('\n')

print('------list.remove()元素移除------')
lst = [1, 1, 2, 1, 2]
lst.remove(1)
print('lst移除元素后结果：', lst)  # 重复元素只移除第一个 元素不存在抛出 ValueError
print('\n')

print('------list.pop()删除一个指定索引位置上的元素------')
lst = [0, 1, 'c', 3, 4]
# lst.pop(1)
print('lst移除指定索引元素后返回结果：', lst.pop(2))  # 返回被移除元素
print('lst移除指定索引元素后结果：', lst)
print('\n')

print('------list切片删除元素------')
lst = [0, 1, 2, 3, 4]
lst2 = lst[1:3:]
print("lst2切片：", lst2)
print('切片删除前lst地址：', id(lst))
lst[1:3:] = []
print('切片删除后lst地址：', id(lst))  # 地址不变
print(lst)
print('\n')
print('------list.clear()清空元素------')
lst = [0, 1, 2, 3, 4]
lst.clear()
print('clear()后结果：', lst)
print('\n')

print('------del lst删除列表------')
lst = [0, 1, 2, 3, 4]
del lst
print('\n')

print('------list列表元素修改------')
lst = [0, 1, 2, 3, 4]
lst[2] = 100
print('一次修改一个元素：', lst)
lst = [0, 1, 2, 3, 4]
lst[1:3] = [99, 88]
print('切片修改，一次修改多个元素：', lst)
lst = [0, 1, 2, 3, 4]
lst[1:3] = [22]
print('切片修改，一次修改多个元素：', lst)
print('\n')

print('------list列表元素排序------')
lst = [0, 4, 2, 3, 1]
print('排序前：', lst)
lst.sort()  # 默认升序排序 reverse=False 不产生新列表对象
print('排序后：', lst)
lst.sort(reverse=True)
print('降序排序后：', lst)

lst = [0, 4, 2, 3, 1]
lst2 = sorted(lst)
print('sorted排序原对象：', lst)
print('sorted排序（产生新对象）：', lst2)
print('\n')

print('------list列表生成式------')
# lst=[i for i in range(0,10)]
lst = [i * 2 for i in range(0, 10)]
print('生成结果：', lst)
