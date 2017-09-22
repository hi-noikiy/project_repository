#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    proxy_middleware for abuyun_proxy
'''

from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
import base64

# proxy_server ip
proxyServer = 'http://proxy.abuyun.com:9010'

# proxy_server authentication
proxyUser = 'HZEV528W24B7O39P'
proxyPass = '020D5CD862A7FC15'

# proxyUser = 'H47L8SXYDPKK7RRP'
# proxyPass = '9FCB7EC7C7ED5FE0'

proxyAuth = "Basic " + base64.urlsafe_b64encode(proxyUser + ":" + proxyPass)

class Proxy_middleware(HttpProxyMiddleware):

    def __init__(self, auth_encoding='latin-1'):
        self.auth_encoding = auth_encoding

    def process_request(self, request, spider):
        print "Ready for Proxy!"
        request.meta['proxy'] = proxyServer
        request.headers['Proxy-Authorization'] = proxyAuth
        request.headers['Proxy-Switch-Ip'] = 'yes'
