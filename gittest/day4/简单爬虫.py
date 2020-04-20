import requests
from bs4 import BeautifulSoup
import queue

start_page = "http://www.163.com"
domain = "163.com"
url_queue = queue.Queue()
seen = set()            #  定义一个集合  集合内数据不重复
seen.add(start_page)
url_queue.put(start_page)


def sotre(url):       #  可以存储到文件内
    pass


def extract_urls(url):   # 爬取url 并解析出来
    urls = []
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    for e in soup.findAll('a'):
        url = e.attrs.get('href', '#')    #  获取url属性 href  就是url
        urls.append(url)
    return urls


while True:

    if not url_queue.empty():

        current_url = url_queue.get()    # 当前队列中的url  get()在队列中取值  队列集合是去重的 seen = set()
        print(current_url)
        sotre(current_url)    #    可以存储爬下来的数据
        for next_url in extract_urls(current_url):
            if next_url not in seen and domain in next_url:  #  判断该url是否在队列中重复，如果不重复加到队列中
                seen.add(next_url)
                url_queue.put(next_url)
    else:
        break
