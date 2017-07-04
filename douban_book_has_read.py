import requests
from lxml import etree
from bs4 import BeautifulSoup
import time
import numpy as np
import json

# use browser to get cookie information
cookie = ''

usr_agents=['Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
     'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11',
     'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)']

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',
    'Host':'book.douban.com',
    'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
            'Connetcting':'keep-alive',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Referer' : 'https://book.douban.com/people/cynthia717/authors',
            'Cache-Control': 'max-age=0'}
cookies = {'cookie': cookie}
#url = 'https://book.douban.com/people/cynthia717/collect?start=0&sort=time&rating=all&filter=all&mode=grid'
#url = 'https://book.douban.com/mine?status=wish'
url='https://book.douban.com/people/cynthia717/collect'
#url = 'http://www.douban.com'
#session = requests.Session()
#r = session.get(url, headers=headers, cookies = cookies)
r = requests.get(url, cookies = cookies, headers = headers)
#opener = urllib.request.build_opener() #自定义opener
#opener.addheaders = [headers] #添加客户端信息
#urllib.request.install_opener(opener) #如解除注释，则可以使用方法2

#data = opener.open(url).read()  #打开方法1
#data=urllib.request.urlopen(url).read()  #打开方法2

#open main page
with open('has_read.html', 'wb+') as f:
   f.write(r.content)

# s = requests.Session()
books = []
#end = 1560
end=1300
for id in range(0, end, 15):
    time.sleep(np.random.rand()*5)
    url = 'https://book.douban.com/people/cynthia717/collect?start=' + str(id)
    #url = 'https://book.douban.com/people/cynthia717/wish?start=' + str(id) + '&sort=time&rating=all&filter=all&mode=grid'
    response = requests.get(url, cookies = cookies, headers = headers)
    print(url)
    #response = s.get(url, cookies = cookies, headers = headers)
    with open('./has_read/douban' + str(id) + '.html', 'wb+') as f:
        f.write(response.content)

    #response = self.session.get(url)
    soup = BeautifulSoup(response.content, "lxml")

    #crawl each comment region
    regions = soup.find('ul', class_="interest-list").find_all('li', class_="subject-item")
    for region in regions:
        book_info = region.find('div', class_ = "info")
        book = {}
        book['title'] = book_info.find('h2').find('a').text.strip()
        book['href'] = book_info.find('h2').find('a')['href']
        book['pub'] = book_info.find('div', class_ = "pub").text.strip()
        short_note = book_info.find('div', class_ = "short-note")
        book['ratings'] = short_note.find_all('span')[0]['class'][0]
        book['read_date'] = short_note.find('span', class_ = 'date').text.strip()
        tag_span = short_note.find('span', class_ = 'tags')
        if tag_span:
            book['tags'] = tag_span.text.strip()
        book['comment'] = short_note.find('p', class_ = 'comment').text.strip()
        books.append(book)
        #comment = region.find('p').text
        #reply_url = region.find('a', class_="lnk-reply").attrs['href']
        print(book)

with open('read_books.json', 'w') as f:
    #f.write(json.dumps(books))
    json.dump(books, f, sort_keys = True, indent = 4, ensure_ascii = False)
