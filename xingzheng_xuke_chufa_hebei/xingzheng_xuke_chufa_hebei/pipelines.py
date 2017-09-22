# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import MySQLdb.cursors
from items import XingzhengXukeHebeiItem,XingzhengChufaHebeiItem
from twisted.enterprise import adbapi
import items

class XingzhengXukeChufaHebeiPipeline(object):
    def __init__(self, dbpool, dbpool1):
        self.dbpool = dbpool
        self.dbpool1 = dbpool1

    @classmethod
    def from_settings(cls, settings):
        dbargs = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            port=settings['MYSQL_PORT'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbargs1 = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME1'],
            port=settings['MYSQL_PORT'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
        dbpool1 = adbapi.ConnectionPool('MySQLdb', **dbargs1)
        return cls(dbpool,dbpool1)

    def process_item(self, item, spider):
        d = self.dbpool.runInteraction(self._do_upinsert, item, spider)
        # if isinstance(item, GonggongziyuanjiaoyiGcjsLanzhouItem):
        #     d = self.dbpool.runInteraction(self._do_upinsert, item, spider)
        # if isinstance(item,ZhengfucaigouYunnanItem_pending):
        #     d = self.dbpool1.runInteraction(self._do_upinsert, item, spider)
        return item

    def _do_upinsert(self, conn, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                print 'NOT ANY DATA IN ITEM'
        if valid:
            item_dict = items.item_dicts
            for i in item_dict:
                if isinstance(item, i):
                    table_name = item_dict[i]
                    field_list = []
                    for field in item:
                        field_list.append(field)
                    result = self.sql_program(conn, table_name, field_list, item)
                    if result:
                        print 'added a record'
                    else:
                        print 'failed insert into ' + table_name

    def sql_program(self, cursor, table_name, field_list, item):
        field_string = ",".join(map(lambda x: '`' + x + '`', field_list))
        item_str = ",".join(map(lambda x: '"' + x + '"', item.values()))
        mysql = 'insert ignore into ' + table_name + '(' + field_string + ')values(' + item_str + ')'
        result = cursor.execute(mysql)
        return result