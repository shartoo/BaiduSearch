# -*- coding:utf-8 -*-
#scrapy 在IDE中的入口
from scrapy import cmdline

keyword = "F:/workspace/python/seCrawler-master/seCrawler/spiders/keyword.txt"
with open(keyword,'r') as read:
    for word in read:
        print("keyword is  ",word)
        cmd ="scrapy crawl keywordSpider -a keyword="+word+" -a se=baidu -a pages=50"
        cmdline.execute(cmd.split())
