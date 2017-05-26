from scrapy.spiders import Spider
from seCrawler.common.searResultPages import searResultPages
from seCrawler.common.searchEngines import SearchEngineResultSelectors
from scrapy.selector import Selector
import scrapy
import html2text
import urllib
import re
import pq
from seCrawler.items import keywordItem
from seCrawler.spiders import util
from seCrawler import send_msg

class keywordSpider(Spider):
    name = 'keywordSpider'
    allowed_domains = ['bing.com','google.com','baidu.com']
    start_urls = []
    keyword = None
    searchEngine = None
    selector = None


    def __init__(self, keyword, se = 'bing', pages = 50,  *args, **kwargs):
        super(keywordSpider, self).__init__(*args, **kwargs)
        self.keyword = keyword.lower()
        self.searchEngine = se.lower()
        self.selector = SearchEngineResultSelectors[self.searchEngine]
        pageUrls = searResultPages(keyword, se, int(pages))
        currUrl = pageUrls.next()
        self.start_urls.append(currUrl)

    def parse_old(self,response):
        realurl_list = []
        select_index = 0
        #summary_extract= response.xpath("//div/a[@target=\"_blank\"]/following-sibling::div[@class=\"c-tools\"]").extract()
        summary_extract= response.xpath("//div/a[@target=\"_blank\"]/following-sibling::*").extract()
        url_all = response.xpath("//div/a[@target=\"_blank\"]").extract()
        for sel in response.xpath("//div/a[@target=\"_blank\"]"):
            tmp_url = sel.extract()
            #url_releated = sel.xpath(".").extract()
            if "http://cache.baiducontent.com" not in tmp_url:
                #print("before extract url is\t",tmp_url)
                if "百度快照" in summary_extract[select_index]:
                    select_index = select_index +1
                if "评价" in summary_extract[select_index]:
                    select_index = select_index +1
                summary = summary_extract[select_index]
                real_url = util.get_redirect_url(tmp_url)
                print("real url is:\t",real_url)
                print("summary is \t",summary)
            select_index = select_index +1

    def parse(self,response):
       divs = response.xpath("//div[@class[contains(.,'result')]]").extract() #使用'.' 而不是 text()来抽取包含
       for div in divs:
           print(div)
           print("=====================")
           part_sel = Selector(text=div)
           href = part_sel.xpath("//a").extract()
           real_url = util.get_redirect_url(href[0])
           print("url is\t",real_url)

           time = part_sel.xpath("//span[@class[contains(.,'newTimeFactor_before_ab')]]").extract()
           if len(time)>0:
            print("time is:  ",util.get_time_from_html(time[0]))
           else:
               gray_time = part_sel.xpath("//span[@class=\"c-gray\"]").extract()
               if len(gray_time)>0:
                print(util.get_time_from_html(gray_time[0]))


    def parse_bk(self, response):
        extract_content = []
        url_list =[]
        realurl_list =[]
        titles =[]
        publish_times =[]
        summarys =[]
        #write.write(response.body)
        #for tmp_url in response.xpath("//div[@class=\"f13\"]").extract():
        for tmp_url in response.xpath("//div/a[@target=\"_blank\"]").extract():
            if "http://cache.baiducontent.com" not in tmp_url:
                url_list.append(tmp_url)
                real_url = self.get_real_url(tmp_url)
                if real_url is not None:
                    tmpPage = requests.get(real_url,allow_redirects=False)
                    if tmpPage.status_code == 200:
                        print("stats_code =200")
                        urlMatch = re.search(r'URL=\'(.*?)\'', str(tmpPage.text.encode('utf-8')), re.S)
                        if urlMatch is not None:
                            realurl_list.append(urlMatch.group(1))
                    elif tmpPage.status_code == 302:
                        redirect_url = tmpPage.headers.get('location')
                        realurl_list.append(redirect_url)
                else:
                    print('No URL found!!')

            for content in response.xpath("//div[@class=\"c-abstract\"]").extract():
                con = self.get_content(content)
                if con not in titles:
                    titles.append(con)
                if con not in summarys:
                    summarys.append(con)
                    print("content :",con)

            for publish_time in response.xpath("//div[@class=\"c-abstract\"]/span/text()").extract():
                publish_time = publish_time.replace("-","")
                if publish_time not in publish_times:
                    publish_times.append(publish_time)
                    print("time :",publish_time)

        with open("search_result.txt","w") as write:
            content =""
            max = min(len(publish_times),len(publish_times),len(summarys))
            for i in range(0,len(realurl_list)):
                content = content + realurl_list[i]+"\n" #+publish_times[i]+"\t"+summarys[i]+"\n"
                # item['publish_time'] = publish_times[i]
                # item['title'] = titles[i]
                # item['summary'] = summarys[i]
            flag = send_msg.send_mail(send_msg.mailto_list,"content from crawl keyword="+"亨斯迈聚氨酯为管道业提供保温解决方案",content)
            if flag:
                print("email send success..")


    def parse_real_url(self,response):
        url = response.url
        print("url from parse is\t",url)
        pass

    def parse_html_body(self,response):
        print("am i called?")
        title = response.xpath('//title').extract()[0].replace("title","").replace(">","").replace("<","").replace("/","")
        print("current title is ",title)
        with open(self.keyword+title,"wb") as write:
            write.write(response.text.encode("utf-8"))
            print("write file done!...")


    def get_content(self,content):
        start_str = "</span>"
        end_str ="</div>"

        start_index = str(content).find(start_str,1)+len(start_str)
        end_index = str(content).find(end_str,start_index)-len(end_str)

        real_con = content[start_index:end_index].replace("<em>","").replace("</em>","")

        return real_con