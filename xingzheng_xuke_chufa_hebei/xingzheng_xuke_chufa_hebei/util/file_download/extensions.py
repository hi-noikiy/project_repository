#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'zhouxiao'

'''
    Scrapy 扩展,挂钩 Scrapy引擎
'''

from scrapy import signals
from scrapy.exceptions import NotConfigured

from file_download import FileDownload, Url_Into_Redis


class Spider_Open_Close_Test(object):
    def __init__(self, *args):
        self.args = args

    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings.getbool('Extensions_Go'):
            raise NotConfigured

        my_name = cls.__name__

        ext = cls(my_name)

        crawler.signals.connect(ext.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(ext.spider_closed, signal=signals.spider_closed)
        crawler.signals.connect(ext.item_scraped, signal=signals.item_scraped)
        crawler.signals.connect(ext.item_dropped, signal=signals.item_dropped)
        # crawler.signals.connect(ext.item_passed, signal=signals.item_passed)

        return ext

    def spider_opened(self, spider):
        for i in self.args:
            spider.log("++++++++++++++++++ For Test +++++++++++++++++")
            spider.log(spider.name)

    def spider_closed(self, spider):
        spider.log("============ For Over =============")
        spider.log("Your_spider is over!")

        spider.log("FileDownload is ready !")
        Redis = Url_Into_Redis(spider.name)
        r_instance = Redis.redis_instance()
        FileDownload.get_urls_set(Redis, 5).filedownload_reay()
        Redis.del_key(r_instance)

    def item_scraped(self, item, spider):
        pass

    def item_dropped(self, item, spider):
        pass

    # def item_passed(self, item, spider):
    #     pass
