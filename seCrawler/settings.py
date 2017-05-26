# -*- coding: utf-8 -*-

# Scrapy settings for seCrawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'seCrawler'

SPIDER_MODULES = ['seCrawler.spiders']
NEWSPIDER_MODULE = 'seCrawler.spiders'

ITEM_PIPELINES = {'seCrawler.pipelines.SespiderPipeline': 1}

USER_AGENT = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"

DEPTH_LIMIT = 1



# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'seCrawler (+http://www.yourdomain.com)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY=10
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN=16
# CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
# COOKIES_ENABLED=False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED=False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'seCrawler.middlewares.MyCustomSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'seCrawler.middlewares.MyCustomDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'seCrawler.pipelines.SomePipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
# AUTOTHROTTLE_ENABLED=True
# The initial download delay
# AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED=True
# HTTPCACHE_EXPIRATION_SECS=0
# HTTPCACHE_DIR='httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES=[]
# HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'


'''下载中间件设置'''
DOWNLOADER_MIDDLEWARES = {
 'scrapy_crawlera.CrawleraMiddleware': 600
}

USER_AGENTS = [
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"\
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",\
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",\
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",\
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",\
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",\
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",\
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

'''下载中间件设置'''
DOWNLOADER_MIDDLEWARES = {
            'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware':None,
            #'baidu.middlewares.RotateUserAgentMiddleware':400,
}

def getCookie():
    cookie_list = [
    'cookie1' #自己从不同浏览器中获取cookie在添加到这
    ]
    cookie = {"B64_BOT":1,"BD_CK_SAM":1,"BD_HOME":1,
              "BD_UPN":"12314753","H_PS_645EC":"02cd6qGTdjIhM34tYFBV6pn%2BpwAdyHGRwl1BQUCzAREcUz3pw%2FdQAstTQtzFhbS0%2BakB5g",
              "ispeed_lsm":2,"rsv_jmp_slow":"1495294619448"}
    #cookie = random.choice(cookie_list)
    return cookie

'''设置默认request headers'''
# DEFAULT_REQUEST_HEADERS = {
#     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#     'Accept-Encoding':'gzip, deflate, sdch',
#     'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
#     'Cache-Control':'max-age=0',
#     'Connection':'keep-alive',
#     'Host':'www.baidu.com',
#     'RA-Sid':'7739A016-20140918-030243-3adabf-48f828',
#     'RA-Ver':'3.0.7',
#     'Upgrade-Insecure-Requests':'1',
#     'Cookie':'%s' % getCookie()
# }

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

COOKIES_ENABLED=False

'''下载延时，即下载两个页面的等待时间'''
DOWNLOAD_DELAY = 2.5

'''并发最大值'''
CONCURRENT_REQUESTS = 100

'''对单个网站并发最大值'''
CONCURRENT_REQUESTS_PER_DOMAIN = 100

'''启用AutoThrottle扩展，默认为False'''
AUTOTHROTTLE_ENABLED = False

'''设置下载超时'''
DOWNLOAD_TIMEOUT = 10

'''降低log级别，取消注释则输出抓取详情'''
LOG_LEVEL = 'INFO'


MYSQL_HOST = '127.0.0.1'
MYSQL_DBNAME = 'crawl'
MYSQL_USER = 'root'
MYSQL_PASSWD = '123456'
# ITEM_PIPELINES = {
#  'seCrawler.pipelines.MySQLStoreKeywordPipeline':400,
# }