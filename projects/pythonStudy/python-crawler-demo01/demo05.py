# coding:utf-8
# @SoftWare PyCharm
# @FileName demo05.py
# @Auther zhanglin
# @Date 2021/05/25/0025 16:52
# @Describe 信息提取demo


from bs4 import BeautifulSoup

import spiderUtil as sp

spider = sp.spider()
soup = BeautifulSoup(spider.crawling('https://www.icourse163.org/'), 'html.parser')
print('---------------------------')
# for link in soup.find_all('p'): # 查找指定标签
#     print(link.get('href'))
for link in soup.find_all(True): # 查找所有标签
    print(link.name)