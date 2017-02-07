# -*- coding: utf-8 -*-
from scrapy import Spider
from json import loads
from scrapy.http.response.text import TextResponse


class NeteaseSpider(Spider):
    name = "Netease"
    start_urls = [
        r'http://bendi.news.163.com/jiangsu/special/04248H8U/wxxxl.js', # Wuxi
        r'http://bendi.news.163.com/jiangsu/special/04248H8U/njxxl.js', # Nanjing
        r'http://bendi.news.163.com/jiangsu/special/04248H8U/szxxl.js', # Suzhou
        r'http://bendi.news.163.com/jiangsu/special/04248H8U/czxxl.js', # Changzhou
        r'http://bendi.news.163.com/jiangsu/special/04248H8U/ntxxl.js'  # Nantong
    ]
    res_template = {
        'body': '''data_callback([ ... ])''',
        'head': 'data_callback(',
        'tail': ')'
    }

    def parse(self, response):
        print type(response)
        print dir(response)
        if response.status == 200 and isinstance(response, TextResponse):
            print type(response.text), type(response.body)
            print response.encoding
            hi, ti = len(self.res_template['head']), -1 * len(self.res_template['tail'])
            body = response.body.strip()[hi:ti]
            news_set = loads(body, encoding=response.encoding)
            for news in news_set:
                print "city:", response.request.url[-8:-6]
                print "title: ", news["title"].encode(response.encoding)
                print "docurl: ", news["docurl"].encode(response.encoding)
                print "time: ", news["time"].encode(response.encoding)
                print ''
        else:
            print 'incorrect response,', response.status
