#coding:utf-8
from scrapy.http import HtmlResponse
import logging
class JsMiddleware(object):
    def process_request(self,request,spider):
        if spider.name=="xingzhengxuke" or spider.name=='xingzhengchufa':
            spider.brower.get(request.url)
            import time
            time.sleep(1)
            # logging.info("访问：{}".format(request.url))
            return HtmlResponse(url=spider.brower.current_url,body=spider.brower.page_source,request=request,encoding='utf-8')
