# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
import ziduan_biao
import buyao_ziduan
import copy

""" 解析横向表格:
    思路:1.获取表格
        2.清洗表头(删除无效行)
        3.还原合并单元格
        4.获取文本,存到二维数组
        5.删除无效列
        6.返回字典列表
        """

def get_table(html):#获取待解析的表格->>(注:传入包含一个有且仅有一个table的html,返回一个table)
    soup_info = BeautifulSoup(unicode(html),"html.parser")
    table_list = soup_info.select('table')
    if table_list:
        return table_list[0]
def clean_head_and_column(table):#清洗表头->>删除无效行->>列表(返回list)
    souptable = BeautifulSoup(unicode(table),"html.parser")
    tr_list = souptable.select("tr")
    table_list_return=[]
    if len(tr_list) > 1:
        for index,tr in enumerate(tr_list):
            souptr = BeautifulSoup(unicode(tr),"html.parser")
            tr_detail = souptr.get_text().encode('utf-8').replace('\n', '').replace(' ', '').replace('\xc2\xa0',
                                                                                                     '').replace('',
                                                                                                                 '').strip()
            td_list = souptr.select("td")
            if len(td_list) <= 1:
                del tr_list[index]
            elif tr_detail is None:
                del tr_list[index]
            elif tr_detail == '':
                del tr_list[index]

        for tr in tr_list:
            souptr = BeautifulSoup(unicode(tr),"html.parser")
            td_list=souptr.select("td")
            table_list_return.append(td_list)
    return table_list_return

def get_huanyuan_table(content_list):#合并单元格,返回一个还原后的table二维数组(他人发现问题,而改)
    rowspan_column={}
    rowspan_td_dict={}
    huanyuan_table=[]
    for td_list in content_list:
        is_one = False
        for ind_lie, td in enumerate(td_list):
            souptd = BeautifulSoup(unicode(td),"html.parser")
            try:
                rowspan_column[ind_lie] = souptd.td['rowspan']
                rowspan_td_dict[ind_lie] = td
                is_one = True
            except Exception, e:
                pass
        if rowspan_td_dict != {} and is_one == False:
            for column,rowspan in zip(rowspan_td_dict,rowspan_column):
                td_list.insert(column, rowspan_td_dict[column])
                rowspan_value=int(rowspan_column[rowspan])
                rowspan_value-=1
                if rowspan_value==1:
                    del rowspan_column[rowspan]
                    continue
        huanyuan_table.append(td_list)
    return huanyuan_table

def get_valid_table(huanyuan_table):#获得有用的待抓取的二维表
    table_value=[]
    for td_list in huanyuan_table:
        td_value_list=[]
        for td in td_list:
            soup=BeautifulSoup(unicode(td),"html.parser")
            td_value =soup.get_text().replace(r'\r', '').replace(r'\n','').replace(' ', '').strip().replace(' ', '').replace('"','').replace('\r','').replace('\n','').decode('unicode_escape').encode('utf-8')
            td_value_list.append(td_value)
        table_value.append(td_value_list)
    return table_value

def delete_invalid_column(field_list,table_value,invalid_list):#删除无效列
    delete_index=[]
    for index,td in enumerate(field_list):
        for arg in invalid_list:
            if td==arg:
                # print td
                delete_index.append(index)
    delete_index.sort()
    delete_index.reverse()
    # print delete_index
    valid_table=[]
    for td_list in table_value:
        try:
            for index in delete_index:

                del td_list[index]
            valid_table.append(td_list)
        except:
            pass

    return valid_table

# def get_field_position(valid_table,chinese_list):#确定字段位置->>返回一个下标list
#     index=[]
#     index_return=[]
#     field_list=valid_table[0]
#     for f in field_list:
#         for lenn in range(0, len(chinese_list)):
#             if f.find(chinese_list[lenn]) >= 0:
#                 index.append(lenn)
#     for i in index:
#         if i not in index_return:
#             index_return.append(i)
#     return index_return

def get_item_dict_list(valid_table,english_list):#返回一个包含多个item字典的list,返回的是字典列表(修正了之前返回的是item对象的list)
    item_list = []
    content_list=valid_table[1:]
    print english_list,'!!!!!!!!!!!!!!!!!!!!',content_list
    for td_list in content_list:
        item_dict = {}
        for index,td in enumerate(td_list):
            # print index,'@@@@@@@@@@@@@@@@@@@@@@@',td
            item_dict[english_list[index]] = td
        item_list.append(item_dict)
    return item_list



def main(html):
    """
    :param html: 包含一个table的html(由xpath得到)
    """
    table = get_table(html)
    table_list_return = clean_head_and_column(table)
    # field_list, content_list = get_field_list(table_list_return)
    huanyuan_table = get_huanyuan_table(table_list_return)
    table_value = get_valid_table(huanyuan_table)
    # index_return = get_field_position(valid_table, chinese_list)
    ziduan_dict = ziduan_biao.get_ziduan_dict()
    english_list = []
    field_ver_list = []
    field_list=table_value[0]
    for field in field_list:
        field = field.replace(' ', '').strip()
        rep = re.finditer('（.*?）|\(.*?\)', field)
        for f in rep:
            # print f.group()
            field = field.replace(f.group(), '')
        field_ver = field
        field_ver_list.append(field_ver.replace('\xe3\x80\x80','').replace('\xc2\xa0', '').replace('\t',''))
    field_list_all=copy.deepcopy(field_ver_list)
    # print field_ver_list,'^^^^^^^^^^^^^^^^^^^'
    ziduan_buyao_list = buyao_ziduan.get_buyaoziduan_list()
    for ziduan_buyao in ziduan_buyao_list:
        if ziduan_buyao in field_ver_list:
            field_ver_list.remove(ziduan_buyao)
    for field_ver in field_ver_list:
        # print field_ver
        for ziduan in ziduan_dict:
            if field_ver in ziduan_dict[ziduan]:

                english_list.append(ziduan)
        # else:
        #     english_list.append('')
    # print english_list
    valid_table = delete_invalid_column(field_list_all,table_value, ziduan_buyao_list)
    item_dict_list=get_item_dict_list(valid_table, english_list)
    return item_dict_list

if __name__ == '__main__':
    pass
    # html = response.xpath('//div[@id="zoom"]//table').extract()
    # item_dict_list = main(html)


