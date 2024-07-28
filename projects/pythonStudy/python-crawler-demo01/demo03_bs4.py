# coding:utf-8
# @SoftWare PyCharm
# @FileName demo03_bs4.py
# @Auther zhanglin
# @Date 2021/05/25/0025 16:04
# @Describe BeautifuSoup4 遍历

from bs4 import BeautifulSoup

import spiderUtil as sp

spider = sp.spider()
soup = BeautifulSoup(spider.crawling('https://www.icourse163.org/'), 'html.parser')

print('---------获取子节点-----------')
# print(soup.head.contents)
# print(len(soup.head.contents))
# print(soup.head.contents[1])
# for content in soup.head.contents:
#     print(content)
# for child in soup.head.children: # 遍历子节点
#     print(child)
print('---------获取父节点-----------')
# print(soup.a.parent)
# print(soup.p.parents)
# for parent in soup.p.parents:
#     if parent is None:
#         print('1:',parent)
#     else:
#         print('2:',parent.name)
print('---------获取平行节点-----------')
# print(soup.a.next_siblings)
for next_sibling in soup.a.next_siblings:
    print(len(next_sibling),type(next_sibling),next_sibling.string is None)
# print(soup.img.next_sibling)