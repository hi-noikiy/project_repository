#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

import scrapy
from scrapy import Selector, signals
from scrapy.spiders import CrawlSpider
from ..items import XingzhengChufaHebeiItem
import urllib
import re
import sys
import time
import os
import random
import urllib2
from urlparse import urljoin
from scrapy.xlib.pydispatch import dispatcher
import parse_item_Beautifulsoup_shu
from selenium import webdriver
# from bs4 import BeautifulSoup
from lxml import etree
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError
import json
reload(sys)
sys.setdefaultencoding("utf-8")

#信用河北---行政处罚
class xingzhengchufa_hebei_Spider(CrawlSpider):
    name = 'xingzhengchufa'
    custom_settings = {
        'ITEM_PIPELINES': {
            # 'hainan_huanping.pipelines.FileDownloadsItem': 1,
            'xingzheng_xuke_chufa_hebei.pipelines.XingzhengXukeChufaHebeiPipeline': 300,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'xingzheng_xuke_chufa_hebei.middlewares.Proxy_middleware': 100,
            'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': 1,
        },
        'Extensions_Go': True,
        'CONCURRENT_REQUESTS': 5,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
    }

    def spider_closed(self, spider):
        self.brower.quit()

    def __init__(self):
        super(xingzhengchufa_hebei_Spider, self).__init__()
        self.start_urls = ['http://www.credithebei.gov.cn/chufaList.jspx']
        self.count=0
        dispatcher.connect(self.spider_closed, signals.spider_closed)
        self.brower = webdriver.PhantomJS(executable_path='/home/lenovo/cici/scrapy/part4/luoman/webdriverbao/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
        # self.brower = webdriver.PhantomJS(executable_path='/home/luoman/manmanluo/luoman/webdriverbao/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')

    def parse(self,response):
        maxpage_string = ''.join(response.xpath('//ul[@id="pa_link"]//li[last()]//text()').extract())
        maxpage_ = ''.join(re.findall(u'1/(.*)页',maxpage_string))
        maxpage=int(maxpage_) if maxpage_ else 0
        print maxpage,'%%%%%%%%%%%%%%%%%%%%%%%%%%%'

        # for page in xrange(1, maxpage+1):
        for page in xrange(4500, 4900 + 1):
            formdata = {
                'pageNo': str(page),
                'object': '',
                'depName': '',
                'keyword': '',
                'captcha': ''
            }
            yield scrapy.FormRequest(url=self.start_urls[0], formdata=formdata, dont_filter=True,
                                     callback=self.parse_next, meta={'page': page})

    def parse_next(self, response):
        page = response.meta['page']
        href_list = response.xpath(u'//a[contains(text(),"查看")]//@href').extract()
        for i in xrange(0, len(href_list)):
            url = urljoin('http://www.credithebei.gov.cn', href_list[i])
            yield scrapy.Request(url=url, dont_filter=True, callback=self.parse_item,errback=self.parse_error,meta={'page':page})


    def parse_item(self, response):
        item_ = XingzhengChufaHebeiItem()
        for key in item_.fields:
            item_[key] = ''

        english_list = ['administrative_license_number','administrative_license_number', 'project_name', 'chufa_typeone','chufa_typetwo',  'licensed_content','licensed_content','punishment_basis','administrative_relative_name','social_credit_code','organization_code','business_registration_code','business_registration_code','tax_registration_number','identification_number','legal_representative','legal_representative','approval_date','licensing_authority','local_code','current_state','shuju_update_date','comment']
        chinese_list = ['行政处罚决定文书文号','行政处罚决定书文号', '处罚名称', '处罚类别1','处罚类别2', '处罚事由','违法违规行为','处罚依据','行政相对人名称','行政相对人代码_1','行政相对人代码_2','行政相对人代码_3','企业注册号','行政相对人代码_4','行政相对人代码_5','法定代表人姓名','负责人','处罚决定日期','处罚机关','地方编码','当前状态','数据更新时间','备注']

        item = parse_item_Beautifulsoup_shu.Item().parse_item(response, english_list, chinese_list, item_)
        item['type']='行政处罚'
        item['province_name']='河北省'
        item['url'] = response.url
        city_list=['石家庄市','唐山市','秦皇岛市','邯郸市','邢台市','保定市','张家口市','承德市','沧州市',
                   '廊坊市','衡水市']
        for city in city_list:
            if city in item['project_name'] or city in item['administrative_relative_name'] or city in item['licensing_authority']:
                item['city_name'] = city
        yield item


    def parse_error(self,failure):
        if failure.check(HttpError):
            response = failure.value.response
            with open('error_chufa_http.txt', 'a') as code:
                code.write(response.url + '\n')
        elif failure.check(DNSLookupError):
            request = failure.request
            with open('error_chufa_dns.txt', 'a') as code:
                code.write(request.url + '\n')
        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            with open('error_chufa_timeout.txt', 'a') as code:
                code.write(request.url + '\n')


# r = requests.get(url)
# sel = Selector(text=r.content)
# if str(r.status_code) == '200':
#     item_ = XingzhengChufaHebeiItem()
#     for key in item_.fields:
#         item_[key] = ''
#
#     english_list = ['administrative_license_number', 'administrative_license_number', 'project_name',
#                     'chufa_typeone', 'chufa_typetwo', 'licensed_content', 'licensed_content',
#                     'punishment_basis', 'administrative_relative_name', 'social_credit_code',
#                     'organization_code', 'business_registration_code', 'business_registration_code',
#                     'tax_registration_number', 'identification_number', 'legal_representative',
#                     'legal_representative', 'approval_date', 'licensing_authority', 'local_code',
#                     'current_state', 'shuju_update_date', 'comment']
#     chinese_list = ['行政处罚决定文书文号', '行政处罚决定书文号', '处罚名称', '处罚类别1', '处罚类别2', '处罚事由', '违法违规行为', '处罚依据',
#                     '行政相对人名称', '行政相对人代码_1', '行政相对人代码_2', '行政相对人代码_3', '企业注册号', '行政相对人代码_4', '行政相对人代码_5',
#                     '法定代表人姓名', '负责人', '处罚决定日期', '处罚机关', '地方编码', '当前状态', '数据更新时间', '备注']
#
#     item = parse_item_Beautifulsoup_shu.Item().parse_item(sel, english_list, chinese_list, item_)
#     item['type'] = '行政处罚'
#     item['province_name'] = '河北省'
#     item['url'] = url
#     city_list = ['石家庄市', '唐山市', '秦皇岛市', '邯郸市', '邢台市', '保定市', '张家口市', '承德市', '沧州市',
#                  '廊坊市', '衡水市']
#     for city in city_list:
#         if city in item['project_name'] or city in item['administrative_relative_name'] or city in item[
#             'licensing_authority']:
#             item['city_name'] = city
#     yield item
#
# else:
#     with open('error_chufa.txt', 'a') as code:
#         code.write(url + '\n' + 'page:' + str(page) + '-----status:' + str(r.status_code) + '\n')

