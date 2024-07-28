# coding:utf-8
# @SoftWare PyCharm
# @FileName spiderUtil.py
# @Auther zhanglin
# @Date 2021/05/25/0025 10:09
# @Describe 爬虫通用代码结构

import os

import requests


class spider(object):
    def __init__(self):
        pass

    def crawling(self, url, params):
        try:
            kv = {'user-agent': 'Mozilla/5.0'}
            r = requests.get(url=url, params=params, headers=kv)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text
        except:
            print(self.url, '爬取失败！code=', r.status_code)

    def crawling(self, url):
        try:
            kv = {'user-agent': 'Mozilla/5.0'}
            r = requests.get(url=url, headers=kv)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text
        except:
            print(self.url, '爬取失败！code=', r.status_code)

    def imgcrawing(self, url, root):
        if '?' in url:
            path = root + (url.split('/')[-1]).split('?')[0]
        else:
            path = root + url.split('/')[-1]
        try:
            if not os.path.exists(root):
                os.mkdir(root)
            if not os.path.exists(path):
                r = requests.get(url)
                with open(path, 'wb') as file:
                    file.write(r.content)
                    return '文件保存成功！'
            else:
                return '文件已存在！'
        except:
            return '爬取失败！'

    def ipinfo(self,ip):
        url = 'http://m.ip38.com/ip.asp?ip='
        try:
            r=  requests.get(url+ip)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text[-500:]
        except:
            return '获取失败！'