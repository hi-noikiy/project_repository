# -*- coding: utf-8 -*-
class Item(object):
    def parse_item(self,response,english_list,chinese_list,item,table):
        # for english,chinese in zip(english_list,chinese_list):
        #     value=""
        #     item[english]=""
        #     value_xpath = unicode('//td[contains(.,"'+chinese+'")]/following::td[1]//text()')
        #     value = ''.join(response.xpath(value_xpath))
        #     if value != "":
        #         item[english]="".join(value).strip().encode('utf-8').replace(' ','').replace('\r','').replace('\t','').replace('\n','').replace('\xc2\xa0','')
        # return item
        # for english, chinese in zip(english_list, chinese_list):
        #     value = ""
        #     item[english] = ""
        #     value_xpath = unicode('//table[@id="inputFormTable"]//td[contains(.,"' + chinese + '")]/following::td[1]//text()')
        #     value = ''.join(response.xpath(value_xpath).extract())
        #     if value != "" and value is not None:
        #         # print value, '---------------', english
        #         item[english] = "".join(value.encode('utf-8').replace('\"', '')).replace(' ', '').replace('\xc2\xa0','').replace('\r', '').replace('\t', '').replace('\n', '').strip()
        # return item

        for i in xrange(0, len(chinese_list)):
            shi_value = ''.join(response.xpath(
                u"{}//td[re:match(translate(string(.),'\r\t\n\xc2\xa0 ',''),'^{}')]/following-sibling::td[1]//text()".format(table,chinese_list[i])).extract()).strip().encode('utf-8').replace("\r", "").replace("\t","").replace("\n", "").replace(" ", "").replace(" ", "").replace('"','秒').replace("'","分")
            if item[english_list[i]] == '':
                # print english_list[i], '^^^', chinese_list[i], '^^^', shi_value
                item[english_list[i]] = shi_value
                # print item[english_list[i]],'______________'
        return item
