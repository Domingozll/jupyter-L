# coding:utf-8
# @SoftWare PyCharm
# @FileName demo04_bs4.py
# @Auther zhanglin
# @Date 2021/05/25/0025 16:30
# @Describe 基于bs4库的HTML格式化和编码

from bs4 import BeautifulSoup

import spiderUtil as sp

spider = sp.spider()
soup = BeautifulSoup(spider.crawling('https://www.icourse163.org/'), 'html.parser')

# print(soup.prettify())  # 格式化

