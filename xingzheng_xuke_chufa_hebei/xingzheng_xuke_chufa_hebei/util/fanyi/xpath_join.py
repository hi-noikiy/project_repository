# -*- coding: utf-8 -*-
# __anthor__ = 'jin'
name=[]
#功能：输出代码
def gong1():
    with open('xpath_file.txt','r') as code:
        line=code.readlines()


        for l in line:
            a="self."+l.strip()+"_xpath=''"
            c = "self." + l.strip() + "_xpath"
            #print a
            b="response.xpath("+c+").extract():"
            #print """item['"""+l.strip()+"""']=\"\""""
            print "for "+l.strip()+" in "+b
            #print "\tprint "+l.strip()
            #print """\titem['"""+l.strip()+"""']=\"\""""+""".join("""+l.strip()+""".encode('utf-8')).strip()"""
            print '\t'+l.strip()+"+="+l.strip()

gong1()
    #         print """{0}_sub = re.findall(r'项目及标段名称(.*?)项目业主', data)
    # {1} = {2}_sub[0]
    # logging.info({3})""".format(l.strip(),l.strip(),l.strip(),l.strip())
print "\n\n"
def gong2():
    with open('xpath_file.txt', 'r') as code:
        line = code.readlines()

        for l in line:
            a = "self." + l.strip() + "_xpath=''"
            c = "self." + l.strip() + "_xpath"
            # print a
            b = "response.xpath(" + c + ").extract()[]"
            #print """item['""" + l.strip() + """']=\"\""""
            print l.strip() + "=" + b
            print """item['""" + l.strip() + """']=\"\"""" + """.join(""" + l.strip()+""".encode('utf-8')).strip()"""
gong2()
print '\n\n'
#功能1;输出数据库%
def a():
    with open('xpath_file.txt', 'r') as code:
        line = code.readlines()
        print len(line)
        value = ""
        for row in range(0, len(line)):
            value += "%s,"
        print value

print '\n\n'
#功能2;输出sql参数
def b():
    with open('xpath_file.txt', 'r') as code:
        line = code.readlines()
        aa=""
        for l in line:
            aa+=l.strip() + ","
        print aa

print '\n\n'
#功能3：创建数据库
def c():
    with open('xpath_file.txt', 'r') as code:
        line = code.readlines()
    with open('xpath_chinese.txt','r') as chine:
        chinese=chine.readlines()
        print "create table if not exists `tax_illegal`("
        print "\t`id` int(11) NOT NULL AUTO_INCREMENT,"
        for l,c in zip(line,chinese):
            print "\t`"+l.strip()+"` varchar(250) DEFAULT NULL COMMENT '"+c.strip()+"',"
        print "\tPRIMARY KEY (`id`),"
        print "\tunique key `unique_key`()"
        print ")ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;"
c()

print '\n\n'
#功能4：pipline:item
def d():
    with open('xpath_file.txt', 'r') as code:
        line = code.readlines()
        for l in line:
            print "item['"+l.strip()+"'],"
a()
b()
d()

print '\n\n'
#功能5：输出item属性
def f():
    with open('xpath_file.txt', 'r') as code:
        line = code.readlines()
        for l in line:
            print l.strip() + '= scrapy.Field()'
f()
print '\n\n'
def g():
    with open('xpath_file.txt', 'r') as code:
        line = code.readlines()
        for l in line:
            print "self."+l.strip()+"""_xpath=''"""
#g()
print '\n\n'
def excel():
    with open('xpath_file.txt', 'r') as code:
        line = code.readlines()
        value=""
        for l in range(1,len(line)+1):
            value+="app["+str(l)+"],"
        print value
#excel()
print '\n\n'
def self():
    with open('xpath_file.txt', 'r') as code:
        line = code.readlines()
    with open('xpath_chinese.txt','r') as chine:
        chinese=chine.readlines()
    for l, c in zip(line, chinese):
        print "self."+l.strip()+"""_xpath="""+"""u'//td[contains(text(),\""""+c.strip()+"""\")]/following-sibling::node()//text()'"""
        #print "self." + l.strip() + """_xpath=""" + """u'//div[@class="sqcx_info"]/div[@class="sqcx_cloumn"][{}]/div[@class="navContent"]//ul[{}]//span[contains(text(),\"""" + c.strip() + """\")]/following-sibling::node()'"""
        #print "self."+l.strip()+"""_xpath="""+"""u'//span[contains(text(),\""""+c.strip()+"""\")]/parent::node()/following-sibling::node()[1]/span/text()'"""
        #print "self."+l.strip()+"""_xpath="""+"""u'//td[contains(text(),\""""+c.strip()+"""\")]/following-sibling::node()/span/text()'"""
        #print "self." + l.strip() + """_xpath=""" + """u'//div[@align="center"]/table[1]//*[contains(text(),\"""" + c.strip() + """\")]/parent::node()/parent::node()/parent::node()/following-sibling::node()//text()'"""

self()
print '\n\n'
def item_():
    with open('xpath_file.txt','r') as code:
        line=code.readlines()
        for l in line:
            print """item['"""+l.strip()+"""']=\"\""""
    print '\n'
    with open('xpath_file.txt', 'r') as code:
        line = code.readlines()
        for l in line:
            # print """item['""" + l.strip() + """']=\"\"""" + """.join(""" + l.strip() + """.encode('utf-8')).strip()"""
            print """item['""" + l.strip() + """']=\"\"""" + """.join(""" + l.strip() + """)"""

print '\n'
def field():
    with open('xpath_file.txt','r') as code:
        line=code.readlines()
        a=''
        for l in line:
            a+="\'"+l.strip()+"\',"
        print a


field()
print '\n\n'
def logging():
    with open('xpath_file.txt','r') as code:
        line=code.readlines()
        for l in line:
            print 'logging.info('+l.strip()+')'
logging()

def etree():
    with open('xpath_file.txt','r') as code:
        line=code.readlines()
        for l in line:
            print  l.strip()+'_all=response.xpath(self.'+l.strip()+'_xpath).extract()'
            print 'if '+l.strip()+"_all:"
            print '\t'+l.strip()+"="+l.strip()+"_all[0]"
            #print """item['""" + l.strip() + """']=\"\"""" + """.join(""" + l.strip() + """.encode('utf-8')).strip()"""
print '\n\n'

def string():
    with open('xpath_file.txt','r') as code:
        line=code.readlines()
        for l in line:
            print l.strip()+"=\'\'"



string()
etree()
item_()