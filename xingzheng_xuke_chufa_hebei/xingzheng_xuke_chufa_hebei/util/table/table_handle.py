#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

class Table_handle(object):

    def __init__(self,name):
        self.name = name
        self.re_ziduan={
            'project_name':u'项目名称|建设单位/项目名称|建设单位／项目名称|^名称$',
            'project_address':u'建设地点|^地点$|项目所在地',
            'publicity_time_limit':u'公示期限|公告时限',
            'investment_total':u'总投资',
            'huanbao_investment':u'环保投资',
            'construction_unit':u'建设单位|承建单位|^单位$',
            'accept_time':u'受理日期|受理时间',
            'huanping_agency':u'环境影响评价机构|环评机构|评价机构',
            'yanshou_jiance_agency':u'验收监测.*单位',
            'project_general_situation':u'项目概况|基本概况|基本情况|^概况$',
            'main_measure_environment_effect':u'主要环境影响及预防或者减轻不良|主要环境影响及预防或减轻不良',
            'huanbao_measure':u'环保措施落实情况|环境保护措施落实情况',
            'industry_category':u'行业类别',
            'project_nature':u'项目性质',
            'approval_number':u'审批文号|批复文号|^文号$|发文编号',
            'whether_accept':u'办理状态',
            'reply_date':u'审批时间|^日期$|发文时间',
            'file_name_huanping_report':u'^文件名称$|^文件题名$|批复名称',
            'construction_scale':u'建设内容',
        }

    def back_items(self,table):
        # tds=table.xpath("(.//tr)[1]//td")
        # if len(tds)==0:
        #     tds = table.xpath("(.//tr)[1]//th")
        # elif len(tds)==1:
        #     tds = table.xpath("(.//tr)[2]//td")
        # if len(tds)<=3:
        #     return self.lie_table(table)
        # else:
        return self.hang_table(table)


    # key,value类型表格
    def table_handle(self, table):
        td_list=table.xpath(".//tr/td")
        item={}
        for key,value in self.re_ziduan.items():
            item[key]=''
        item['File_Path']=''
        item['download_link_huanping_report']=''
        for i in xrange(len(td_list)-1):
            td_text=self.join_extract(td_list[i].xpath(".//text()"))
            for key,value in self.re_ziduan.items():
                if re.findall(value,td_text):
                    item[key]=self.join_extract(td_list[i+1].xpath(".//text()"))
        return item

    # 横向表格，最基本的表格
    def hang_table(self, table):
        flag='False'
        # print 'hang------------------'
        tr_list = table.xpath(".//tr")
        # print len(tr_list),'&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'
        td_list = table.xpath(".//tr")[0].xpath("./td")
        if len(td_list)==0:
            flag='True1'
            td_list = table.xpath(".//tr")[0].xpath("./th")
        elif len(td_list)==1:
            flag = 'True2'
            td_list = table.xpath(".//tr")[1].xpath("./td")
        # print len(td_list),'********************************'
        item_list = []
        for i in xrange(1, len(tr_list)):
            # print len(tr_list),'%%%%%%%%%%%%%%%%%%%%'
            if self.join_extract(table.xpath("(.//tr)[{}]//text()".format(i+1))).replace("\r", "").replace("\t", "").replace("\n", "").replace(' ', '') == '' or len(table.xpath("(.//tr)[{}]//td".format(i+1)).extract())<len(td_list):
                continue
            # print '%%%%%%%%%%%%%%%%%%%%'
            # print len(td_list),'###################'
            item = {}
            if flag=='True2':
                # print '%%%%%%%%%%%%%%%%%%%%'
                if i==len(tr_list)-1:
                    continue
                if i<len(tr_list)-1:
                    i+=1
            item['Download_url'] = ''.join(table.xpath("(.//tr)[{}]//a/@href".format(i + 1)).extract())
            print len(td_list),'###################'
            for j in xrange(len(td_list)):
                # print '%%%%%%%%%%%%%%%%%%%%'
                if flag=='True1':
                    td_text = self.join_extract(tr_list[0].xpath("./th")[j].xpath(".//text()")).replace(' ','').replace(' ','')
                elif flag=='True2':
                    td_text = self.join_extract(tr_list[1].xpath("./td")[j].xpath(".//text()")).replace(' ','').replace(' ','')
                else:
                    td_text = self.join_extract(tr_list[0].xpath("./td")[j].xpath(".//text()")).replace(' ','').replace(' ','')

                for key, value in self.re_ziduan.items():
                    if re.findall(value, td_text):
                        # href=self.join_extract(tr_list[i].xpath("./td")[j].xpath(".//a/@href"))
                        # if href:
                        #     item[key] = href
                        # else:
                        item[key] = self.join_extract(tr_list[i].xpath("./td")[j].xpath(".//text()"))
                        print item[key],'^^^^^^^^^^^^^'
            item_list.append(item)
        # print item_list,'###########'
        return item_list

    # 纵向表格，简单,无表中表
    def lie_table(self, table):
        # 列开始数
        m = 0
        # 若第一列不需要则去除
        if '序号' in self.join_extract(table.xpath("(.//tr)[1]/td[1]//text()")):
            m = 1
        trs = table.xpath(".//tr")
        tds = table.xpath("(.//tr)[1]//td")
        item_list = []
        for j in xrange(m+1, len(tds)):# 从第m+1列开始
            item = {}
            for i in xrange(len(trs)):# 行开始
                ziduan = self.join_extract(table.xpath("(.//tr)[{}]/td[{}]//text()".format(i+1, m+1))).replace("\r", "").replace("\t", "").replace("\n", "").replace('　','').replace(' ','')
                shuju = self.join_extract(table.xpath("(.//tr)[{}]/td[{}]//text()".format(i+1, j+1))).replace("\r", "").replace("\t", "").replace("\n", "").replace('　','').replace(' ','')
                for key, value in self.re_ziduan.items():
                    if re.findall(value, ziduan):
                        item[key] = shuju
            item_list.append(item)
        return item_list

    def join_extract(self, m):
        return ''.join(m.extract()).strip().replace('\n', '').replace('\r', '').replace('\t', '').replace(' ', '')






