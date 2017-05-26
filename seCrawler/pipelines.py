# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import logging
from seCrawler import settings
from twisted.enterprise import adbapi
from seCrawler.items import  keywordItem

class SespiderPipeline(object):
    def __init__(self):
        self.file = open('urls.txt', 'w')
        #self.bloomFilter = rBloomFilter.rBloomFilter(100000, 0.01, 'bing')

    def process_item(self, item, spider):
        self.file.write(item['url']+'\n')
        return item

# class MySQLStoreKeywordPipeline(object):
#     def __init__(self, dbpool):
#         self.dbpool = dbpool
#
#     @classmethod
#     def from_settings(cls, settings):
#         dbargs = dict(
#             host=settings['MYSQL_HOST'],
#             db=settings['MYSQL_DBNAME'],
#             user=settings['MYSQL_USER'],
#             passwd=settings['MYSQL_PASSWD'],
#             charset='utf8',
#             #cursorclass = MySQLdb.cursors.DictCursor,
#             use_unicode= True,
#         )
#         print("执行插入操作...")
#         dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
#         return cls(dbpool)
#
#     #pipeline默认调用
#     def process_item(self, item, spider):
#         print("开始处理items..")
#         d = self.dbpool.runInteraction(self._do_upinsert, item, spider)
#         d.addErrback(self._handle_error, item, spider)
#         d.addBoth(lambda _: item)
#         return d
#     #将每行更新或写入数据库中
#     def _do_upinsert(self, conn, item, spider):
#         print("exect insert ")
#         print("insert into keyword_result\(url,title, publish_time, summary\) values\(%s, %s, %s,%s\)
#             "%(item['url'], item['title'], item['publish_time'],item['summary']))
#         conn.execute("""
#                 insert into keyword_result(url,title, publish_time, summary)
#                 values(%s, %s, %s,%s)
#             """, (item['url'], item['title'], item['publish_time'],item['summary']))
#
#
#     #异常处理
#     def _handle_error(self, failue, item, spider):
#         #log.err(failure)
#         pass