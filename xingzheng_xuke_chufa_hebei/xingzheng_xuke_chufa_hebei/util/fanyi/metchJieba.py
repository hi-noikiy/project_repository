#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 3/31/17
@Author  : liushanshan
@Site    : 
@File    : metchJieba.py
@Remark  : 结巴分词匹配文件名和项目名
"""


import jieba


class MetchJiebaParse(object):

    def metching(self, name, name_list):
        # 下列 name, name_list 为测试用：
        # name = '新型建筑钢结构体系及彩钢隔热夹芯板生产项目'
        # name = '甘肃天水百花小镇项目'
        # name = '天水·晟世珑庭项目'
        # name_list = ['新型建筑钢结构体系及彩钢隔热夹芯板生产项目环评报告表', '天水·晟世珑庭项目环评报告书', '天水百花小镇环评报告书']
        # name_list = ['新型建筑钢结构体系及彩钢隔热夹芯板生产项目环评报告表']
        data_list = list()
        for i in xrange(0, len(name_list)):
            str1 = '/'.join(jieba.cut(name))
            str2 = '/'.join(jieba.cut(name_list[i].replace(' ', '')))
            # print str1, '^^^^^^', str2
            list1 = str1.split('/')
            list2 = str2.split('/')
            item_list = [val for val in list1 if val in list2]
            l = len(item_list)
            l=l/float(len(list2))
            # print '交集：', item_list, '交集长度：', l
            data_list.append({l: name_list[i]})
        max_len = 0
        max_name = ''
        for key in xrange(0, len(data_list)):
            # print 'everyone：', key, data_list[key].keys(), data_list[key]
            f = lambda x, y: x if x > y else y
            max_len = f(data_list[key].keys()[0], max_len)
            # print 'max_len：', max_len
            f2 = lambda k, v: data_list[key].values() if k in data_list[key].keys() else v
            max_name = f2(max_len, max_name)
            # print 'max_name：', max_name
        if len(data_list) == 1:
            max_len = data_list[0].keys()
            max_name = data_list[0].values()
            # print '1-max_len：', max_len
            # print '1-max_name：', max_name
        return ''.join(max_name)


if __name__ == '__main__':
    pass
    # result = MetchJiebaParse().metching()
    # print 'result：', result



