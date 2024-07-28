# coding:utf-8
# @SoftWare PyCharm
# @FileName demo03.py
# @Auther zhanglin
# @Date 2021/05/21/0021 9:10
# @Describe 类的浅拷贝和深拷贝

class CPU:
    def __init__(self):
        pass
class Disk:
    def __init__(self):
        pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu = cpu
        self.disk = disk
print('-----------对象的赋值-------------')
cpu1 = CPU()
cpu2 = cpu1
print('对象的赋值：',cpu1 is cpu2)
print('对象的赋值：',cpu1 == cpu2)
print('---------对象的赋值--end----------')
print('\n')

print('----------类的拷贝--------------')
# 浅拷贝：python拷贝一般都是浅拷贝，拷贝时，对象包含的子对象内容不拷贝，因此，源对象和拷贝对象会引用同一子对象。
# 深拷贝：使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象，源对象和拷贝对象所有的子对象引用也会不相同。
cpu = CPU()
disk = Disk()
c1 = Computer(cpu,disk)

import copy
c2 = copy.copy(c1)
c3 = copy.deepcopy(c1)
print('源对象：',c1,c1.cpu,c1.disk)
print('浅拷贝：',c2,c2.cpu,c2.disk)
print('深拷贝：',c3,c3.cpu,c3.disk)

print('--------类的拷贝--end-----------')
print('\n')
