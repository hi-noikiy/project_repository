# -*- coding: utf-8 -*-
# __anthor__ = 'jin'
def translationChtoEn(list):
    import urllib2
    import json
    import urllib

    while True:
        content = list
        if content == 'Q':
            break
        else:
            url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/'
            data = {}

            data['type'] = 'AUTO'
            data['i'] = content
            data['doctype'] = 'json'
            data['xmlVersion'] = '1.8'
            data['keyfrom'] = 'fanyi.web'
            data['ue'] = 'UTF-8'
            data['action'] = 'FY_BY_CLICKBUTTON'
            data['typoResult'] = 'true'

            data =  urllib.urlencode(data)
            response = urllib2.urlopen(url, data)
            html = response.read().decode('utf-8')
            target = json.loads(html)
            # print target
            # print "________"
            results = target['translateResult'][0][0]['tgt']
            # print(results)
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
