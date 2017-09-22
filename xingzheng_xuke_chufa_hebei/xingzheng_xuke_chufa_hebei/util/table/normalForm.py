#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 4/10/17
@Author  : liushanshan
@Site    : 
@File    : normalForm.py
@Remark  : 普通横表解析
"""

class normalForm(object):
    """
    :param: response
    """

    def __init__(self):
        self.item_dict = {
            u"备案号": "beian_number",
            u"项目名称": "project_name",
            u"项目名称*": "project_name",
            # u"文件名": "project_name",
            # u"县": "project_address",
            # u"县别": "project_address",
            u"区域 ": "project_address",
            u"建设地点": "project_address",
            u"建设地址": "project_address",
            # u"所属县市区": "project_address",
            # u"单位": "construction_unit",
            u"单位名称": "construction_unit",
            u"建设单位": "construction_unit",
            u"项目单位": "construction_unit",
            u"企业名称": "construction_unit",
            u"申报单位": "construction_unit",
            u"环评机构": "huanping_agency",
            u"环评单位": "huanping_agency",
            u"评价机构": "huanping_agency",
            u"环境影响评价机构": "huanping_agency",
            u"验收单位": "yanshou_jiance_agency",
            u"验收监测单位": "yanshou_jiance_agency",
            u"验收监测（调查）单位": "yanshou_jiance_agency",
            u"项目概况": "project_general_situation",
            u"基本概况": "project_general_situation",
            u"基本情况": "project_general_situation",
            u"建设概况": "project_general_situation",
            u"建设项目概况": "project_general_situation",
            u"主要环境影响及预防或者减轻不良环境影响对策和措施": "main_measure_environment_effect",
            u"主要环境影响及预防或减轻不良环境影响的对策和措施": "main_measure_environment_effect",
            u"主要环境影响及预防或者减轻不良环境影响的对策和措施": "main_measure_environment_effect",
            u"主要环境影响及预防或者减轻不良环境影响的对错和措施": "main_measure_environment_effect",
            u"环境影响评价文件提出的主要环境影响及预防或者减轻不良环境影响的对策和措施": "main_measure_environment_effect",
            u"环保措施落实情况":"huanbao_measure",
            u"环境保护措施落实情况": "huanbao_measure",
            u"核定排放量": "check_ratify_emissions",
            u"核定污染物种类及排放限值": "check_ratify_emissions",
            u"批复名称": "file_name_huanping_report",
            u"文件名称": "file_name_huanping_report",
            u"审批文件名称": "file_name_huanping_report",
            u"环评文件名称": "file_name_huanping_report",
            u"文号": "approval_number",
            u"文件号": "approval_number",
            u"环评批复": "approval_number",
            u"审批文号": "approval_number",
            u"环评批复文号": "approval_number",
            u"验收审批文号": "approval_number",
            u"文号（吕环行审）": "approval_number",
            u"批复文号（吕环行审）": "approval_number",
            u"批复文号 （吕环行审）": "approval_number",
            u"文件编号(2013)吕环行审": "approval_number",
            u"文件编号(2014)吕环行审": "approval_number",
            u"审批时间": "reply_date",
            u"审批日期": "reply_date",
            u"批复日期": "reply_date",
            u"发文日期": "reply_date",
            u"发文时间": "reply_date",
            u"办理时间": "reply_date",
            # u"公示电子版": "download_link_huanping_report",
            # u'报告书（表）链接': "download_link_huanping_report",
            # u"审批文件全文链接": "download_link_huanping_report",
            # u"环评文件脱密全本": "download_link_huanping_report",
            # u"环评报告书（表）全本链接": "download_link_huanping_report",
            u"受理时间": "accept_time",
            u"受理日期": "accept_time"
        }

    def parser_item(self, response, table_xpath):
        tr_first = 2
        items_list = list()
        trs = response.xpath("{}//tr".format(table_xpath)).extract()
        for r1 in xrange(1, 4):
            tds = response.xpath("({}//tr)[{}]//td".format(table_xpath, r1)).extract()
            tr1_detail = ''.join(
                response.xpath("({}//tr)[{}]//text()".format(table_xpath, r1)).extract()).strip().replace(
                u'\xa0', '').replace(u'\r', '').replace(u'\t', '').replace(u'\n', '').replace(u' ', '')
            # 第一行为空白时，遍历数据从下行开始
            # if (tr1_detail == '' or u'附表' in tr1_detail) and len(tds) >= 2:
            if tr1_detail == '':
                tr_first = tr_first + 1
                print tr_first,'!!!!!!!!',r1
            # 第一行 td<2 时，遍历数据从下行开始
            elif len(tds) <= 2:
                tr_first = tr_first + 1
                # print tr_first,'@@@@@@@@@'
        # print 'tr_first: ', tr_first, '^'*40, len(trs)
        for r in xrange(tr_first, len(trs) + 1):
            items = list()
            tds = response.xpath("({}//tr)[{}]//td".format(table_xpath, r)).extract()
            if len(tds) > 2:
                # print len(tds),'%%%%%%%%%%%%%%%%%%%'
                Download_href = response.xpath("({}//tr)[{}]//a/@href".format(table_xpath, r)).extract()
                if Download_href:
                    Download_url=''
                    # print Download_href,'**********href***********'
                    for href in Download_href:
                        Download_url+=href+','
                    # print Download_url,'^^^^^^^^^^^^^^url^^^^^^^^^^^^^^'
                    items.append({'Download_url':Download_url})
                for d in xrange(1, len(tds) + 1):
                    # 第一行为非表头时，匹配表头从第二行开始，依次类推
                    shi_key = ''.join(response.xpath("({}//tr)[{}]//td[{}]//text()".format(table_xpath, tr_first - 1, d)).extract()).replace(u'\xa0', '').replace(u'\r', '').replace(u'\t', '').replace(u'\n', '').replace(u' ', '')
                    shi_value = ''.join(response.xpath("({}//tr)[{}]//td[{}]//text()".format(table_xpath, r, d)).extract()).replace(u'\xa0', '').replace(u'\r', '').replace(u'\t', '').replace(u'\n', '').replace(u' ', '')
                    # print shi_key, '^^^^^^', shi_value
                    if shi_key in self.item_dict and shi_value != '':
                        # print shi_key, '^^^^^^', shi_value
                        items.append({self.item_dict[shi_key]: shi_value})
                if len(items) > 0:
                    items_list.append(items)
        return items_list

if __name__ == '__main__':
    pass

