# -*- coding:utf-8 -*-
'''
tools method
'''

import re
import requests

def get_real_url(urlstr):
    '''
      get redirect url from urlstr
    :param urlstr:
    :return:
    '''
    start ="href="
    end =" "
    start_index = str(urlstr).find(start,1)+len(start)
    end_index = str(urlstr).find(end,start_index)-1
    real_url = urlstr[start_index:end_index].replace("\"","").strip()
    if "http" not in real_url:
        return None
    else:
        return real_url


def get_redirect_url(tmp_url):
    real_url = get_real_url(tmp_url)
    if real_url is not None:
        tmpPage = requests.get(real_url,allow_redirects=False)
        if tmpPage.status_code == 200:
            print("stats_code =200")
            urlMatch = re.search(r'URL=\'(.*?)\'', str(tmpPage.text.encode('utf-8')), re.S)
            if urlMatch is not None:
                real_url = urlMatch.group(1)
        elif tmpPage.status_code == 302:
            redirect_url = tmpPage.headers.get('location')
            real_url = redirect_url

    return real_url

def get_time_from_html(html):
    index_start = html.find(">")+1
    index_end = html.find("</span>")

    return html[index_start:index_end]