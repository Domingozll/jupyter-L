# coding:utf-8
# @SoftWare PyCharm
# @FileName demo01.py
# @Auther zhanglin
# @Date 2021/05/21/0021 14:44
# @Describe python模块编程

# 第三方模块的安装 pip install 模块名
# 第三方模块的使用 import 模块名

import calc #导入前需要把模块所在目录改为source root
import calc2 #导入前需要把模块所在目录改为source root
from calc import str
# print(calc.add(1,2))
# print(calc.str)
# print(str)

print(calc2.add(10,20))


