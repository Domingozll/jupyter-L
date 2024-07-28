# coding:utf-8
# @SoftWare PyCharm
# @FileName demo06_re.py
# @Auther zhanglin
# @Date 2021/05/26/0026 10:01
# @Describe re正则表达式库

import re
# re.search(pattern, string, flags=0)) 在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象
#        ∙ pattern : 正则表达式的字符串或原生字符串表示
#        ∙ string : 待匹配字符串
#        ∙ flags : 正则表达式使用时的控制标记:
#                 re.I re.IGNORECASE 忽略正则表达式的大小写，[A‐Z]能够匹配小写字符
#                 re.M re.MULTILINE 正则表达式中的^操作符能够将给定字符串的每行当作匹配开始
#                 re.S re.DOTALL 正则表达式中的.操作符能够匹配所有字符，默认匹配除换行外的所有字符
match = re.search(r'[1-9]]\d{5}','BIT100081 TSU100084')
if match:
    print(match.group(0))
# e.match(pattern, string, flags=0) 从一个字符串的开始位置起匹配正则表达式，返回match对
ls = re.match(r'[1-9]\d{5}','100081 BIT')
print(ls.group(0))
# re.findall(pattern, string, maxsplit=0, flags=0) 搜索字符串，以列表类型返回全部能匹配的子串
ls = re.findall(r'[1-9]\d{5}','BIT100081 TSU100084')
print(ls)
# re.split(pattern, string, maxsplit=0, flags=0) 将一个字符串按照正则表达式匹配结果进行分割，返回列表类型
# re.finditer() 搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象
# re.sub() 在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串




