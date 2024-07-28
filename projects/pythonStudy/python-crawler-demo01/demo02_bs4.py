# coding:utf-8
# @SoftWare PyCharm
# @FileName demo02_bs4.py
# @Auther zhanglin
# @Date 2021/05/25/0025 11:45
# @Describe beautifulsoup 基本元素

from bs4 import BeautifulSoup

import spiderUtil as sp

spider = sp.spider()
soup = BeautifulSoup(spider.crawling('https://www.icourse163.org/'), 'html.parser')
print('----------soup.a--------------')
print(soup.a)
print('-----------soup.a.name-------------')
print(soup.a.name)
print('-----------soup.a.parent.name-------------')
print(soup.a.parent.name)
print('-----------soup.a.parent.parent.name-------------')
print(soup.a.parent.parent.name)
print('----------soup.a.attrs--------------')
print(soup.a.attrs)
print('----------soup.a.attrs[\'href\']--------------')
print(soup.a.attrs['href'])
print('----------soup.a.attrs[\'target\']--------------')
print(soup.a.attrs['target'])
print('----------soup.title.string--------------')
print(soup.title.string)
