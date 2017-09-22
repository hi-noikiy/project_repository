# -*- coding: utf-8 -*-
# __anthor__ = 'jin'
import time
def translationChtoEn(list):
    import urllib2
    import json
    import urllib

    while True:
        content = list
        if content == 'Q':
            break
        else:
            url = 'http://fanyi.baidu.com/v2transapi'
            data = {}

            data['from'] = 'zh'
            data['query'] = content
            data['to'] = 'en'
            data['transtype'] = 'translang'
            data['simple_means_flag'] = '3'

            data =  urllib.urlencode(data)
            response = urllib2.urlopen(url, data)

            html = response.read().decode('utf-8')
            # print html
            target = json.loads(html)
            # print target
            # print "________"
            results = target['trans_result']["data"][0]["dst"]
            # print(results)
            time.sleep(1)
            return results

def get_EnglishTitleName(titleList):
    titleEnName = []
    for i in range(len(titleList)):
        titleEnName.append(translationChtoEn(titleList[i]))
        titleEnName[i] = titleEnName[i].title()             #首字母大写
        titleEnName[i] = titleEnName[i].replace(' ', '_')
        titleEnName[i] = titleEnName[i].replace('(', '_')
        titleEnName[i] = titleEnName[i].replace(')', '')
        titleEnName[i] = titleEnName[i].replace(',', '')
        titleEnName[i] = titleEnName[i].replace('/', '_')
        titleEnName[i] = titleEnName[i].replace('.', '')
        titleEnName[i] = titleEnName[i].replace('-', '_')
    return titleEnName

if __name__=='__main__':
    with open('xpath_chinese.txt','r') as chine:
        chinese=chine.readlines()
    titleList=[]
    for c in chinese:
        if c!='\n':
            print c.strip()
            titleList.append(c.strip())
    englishTitleName = get_EnglishTitleName(titleList)
    for e in englishTitleName:
        print e
