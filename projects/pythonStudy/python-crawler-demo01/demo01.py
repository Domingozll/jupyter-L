# coding:utf-8
# @SoftWare PyCharm
# @FileName demo01.py
# @Auther zhanglin
# @Date 2021/05/24/0024 17:47
# @Describe 爬虫demo01

import spiderUtil as sp
spider = sp.spider()
# print(spider.crawling('http://www.baidu.com/s',{'wd':'张琳'}))
print(spider.imgcrawing('https://fwyz.mem.gov.cn//1591058858887_987.JPG',
                         './img/'))

