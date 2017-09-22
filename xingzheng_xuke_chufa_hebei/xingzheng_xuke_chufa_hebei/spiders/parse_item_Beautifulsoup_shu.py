# -*- coding: utf-8 -*-
class Item(object):
    def parse_item(self,response,english_list,chinese_list,item):
        for i in xrange(0, len(chinese_list)):
            shi_value = ''.join(response.xpath(
                u"//div[@class='p10']//table//td[re:match(translate(string(.),'\r\t\n\xc2\xa0 ',''),'^{}')]/following-sibling::td[1]//text()".format(chinese_list[i])).extract()).strip().encode('utf-8').replace("\r", "").replace("\t","").replace("\n", "").replace(" ", "").replace(" ", "").replace('"',"'")
            if item[english_list[i]] == '':
                # print english_list[i], '^^^', chinese_list[i], '^^^', shi_value
                item[english_list[i]] = shi_value
        return item
