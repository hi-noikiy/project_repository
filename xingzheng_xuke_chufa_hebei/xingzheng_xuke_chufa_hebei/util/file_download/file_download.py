#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'zhouxiao'

'''
    类的构建, url = "www.baidu.com', '/home/zhouxiao/Desktop/lala.txt"  ========>>>>>>>中间以 ',' 加 ' ' 拼接
                        url                      file_path
'''


import redis
import threadpool
import urllib
import re
import requests
import os
# import pdfkit
from uuid import uuid1
from time import time

class Url_Into_Redis(object):
    def __init__(self, name):
        self.name = name
        self.pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)

    def redis_instance(self):
        r = redis.StrictRedis(connection_pool=self.pool)
        return r

    def push_url(self, r, file_url):
        r.sadd(self.name, file_url)

    def file_url_set(self, r, name):
        return r.smembers(name)

    def del_key(self, r):
        r.delete(self.name)


class FileDownload(object):
    def __init__(self, urls_set, poolsize):
        self.urls_set = urls_set
        self.pool = threadpool.ThreadPool(poolsize)
        self.done_count=0
        self.down1_count = 0
        self.down2_count = 0
        self.down3_count = 0

    @classmethod
    def get_urls_set(cls, rr, poolsize):
        return cls(rr.file_url_set(rr.redis_instance(), rr.name), poolsize)

    def file_download(self, args):
        args_list = args.split(', ')
        # urllib.urlretrieve(args_list[0], args_list[1])
        # print '下载一个文件,{}'.format(time())
        path = os.environ['HOME'] + args.split(', ')[1]
        file = os.path.join(os.environ['HOME'] + args.split(', ')[1], args.split(', ')[2])
        # file_name = str(uuid1())
        # file1 = os.path.join(os.environ['HOME'] + args.split(', ')[1], file_name)
        downType=args_list[3]
        if not os.path.exists(file):
            if downType == '下载1':
                try:
                    self.down1_count += 1
                    r = requests.get(args_list[0])
                    with open(file, 'wb') as code:
                        code.write(r.content)
                    print '---------------Download------------', self.down1_count
                    # urllib.urlretrieve(args_list[0], file)
                except:
                    with open('error.txt', 'a') as code:
                        code.write(file + '\n')
            elif downType == '下载2':
                suffix=''
                r = requests.get(args_list[0])
                try:
                    head=r.headers['Content-Disposition'].replace('"','')
                    suffix=head[head.rfind('.'):]
                    if '?' in suffix:
                        suffix=suffix[:suffix.rfind('?')]
                    with open(file+suffix,'wb') as code:
                        code.write(r.content)
                    self.down2_count += 1
                    print '---------------Download2------------',self.down2_count
                except:
                    with open('error.txt','a') as code:
                        code.write(file+suffix+'\n')
            elif downType == '下载3':
                try:
                    self.down1_count += 1
                    postdata={'fileName':args_list[4],'filePath':args_list[5]}
                    r = requests.post(args_list[0],postdata)
                    with open(file, 'wb') as code:
                        code.write(r.content)
                    print '---------------Download3------------', self.down1_count
                    # urllib.urlretrieve(args_list[0], file)
                except:
                    with open('error.txt', 'a') as code:
                        code.write(file + '\n')

    def filedownload_reay(self):
        requests = threadpool.makeRequests(self.file_download, list(self.urls_set))
        [self.pool.putRequest(req) for req in requests]
        self.pool.wait()


# if __name__ == '__main__':
#     Redis = Url_Into_Redis('test_for_class')
#     r_instance = Redis.redis_instance()
#     Redis.push_url(r_instance, "http://zhaotoubiao.sipac.gov.cn/yqztbweb/ReadAttachFile.aspx?AttachID=9cedf8be-5c6f-433c-b363-b70d694b0536, /home/zhou/Desktop/1.pdf")
#     Redis.push_url(r_instance, "http://zhaotoubiao.sipac.gov.cn/yqztbweb/ReadAttachFile.aspx?AttachID=5f39e2e3-823e-4a3b-afa8-03a68bdec5a2, /home/zhou/Desktop/2.pdf")
#
#     FileDownload.get_urls_set(Redis, 10).filedownload_reay()
#     Redis.del_key(r_instance)
    # print FileDownload.get_urls_set(Redis, 10).urls_set







