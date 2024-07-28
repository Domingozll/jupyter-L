# coding:utf-8
# @SoftWare PyCharm
# @FileName demo03_bool.py
# @Auther zhanglin
# @Date 2021/05/14/0014 19:17
# @Describe

# python所有对象都有一个布尔值
# 以下对象布尔值为False
print('-------------以下对象布尔值为False-----------------')
# False
print('False', bool(False))
# 空数值（）
print('空数值（）bool(0)', bool(0))
print('空数值（）bool(0.0)', bool(0.0))
# None
print('None', bool(None))
# 空字符串
print('空字符串\'\'', bool(''))
print('空字符串\"\"', bool(""))
# 空列表
print('空列表list()', bool(list()))
print('空列表[]', bool([]))
# 空元组
print('空元组()', bool(()))
print('空元组tuple()', bool(tuple()))
# 空字典
print('空字典dict()', bool(dict()))
print('空字典dict()', bool({}))
# 空集合
print('空集合set()', bool(set()))
print('-------------其他对象布尔值为True-----------------')
