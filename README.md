use python3

豆瓣被点名批评，会不会被封呢。傻TT就很纠结这个问题，作为程序员的我只能写个脚本给她备份数据。

后续的页面美观数据查询等问题再说。

主要备份看过的书(douban_book_has_read.py)和想看的书部分(douban_book_want_read.py)。
这两个文件基本一样，只是某些解析页面结构部分有很小的差别。
比如想看的书没有rating，看过的书有rating。

## 值得注意的：
+ 睡眠：`time.sleep(np.random.rand()*5)`
+ 一开始想看的书总是返回403，抓狂了，以为不应该用requests.get,然后尝试了用seesion.get,urllib.get之类的。我傻吗，显然本质问题不在这里，这些函数底层显然是一样，requests.get不能用，其余也不能用啊。
没有仔细看headers和真实浏览器相比缺少什么就是我最大失误。
为了这个问题纠结了很久。
后来发现，其实很简单，就是缺少Referer的header（看你浏览器缓存指定）
```
'Referer' : 'https://book.douban.com/people/cynthia717/authors'
```
很无奈，这个问题纠结了快一两个小时，就是没有仔细想清楚到底什么问题就瞎尝试。
+ User-Agent就是基本
+ 一开始又想用scrapy,但是还是最简单的requests.get最好用，反正我的需求量也不大，不需要多线程，数据库等。

### 是否需要登录问题（不需要，403不是登录问题）
还以为有些数据爬要登录，[七月算法课程《python爬虫》第四课: 相关库使用与登录问题](http://blog.csdn.net/NNNNNNNNNNNNY/article/details/53976875)发现可以：

```
import requests
import html5lib
import re
from bs4 import BeautifulSoup


s = requests.Session()
url_login = 'http://accounts.douban.com/login'

formdata = {
    'redir':'https://www.douban.com',
    'form_email': 'liyanan001@yeah.net',
    'form_password': 'xxxxxx',
    'login': u'登陆'
}
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}

r = s.post(url_login, data = formdata, headers = headers)
content = r.text
soup = BeautifulSoup(content, 'html5lib')
captcha = soup.find('img', id = 'captcha_image')
if captcha:
    captcha_url = captcha['src']
    re_captcha_id = r'<input type="hidden" name="captcha-id" value="(.*?)"/'
    captcha_id = re.findall(re_captcha_id, content)
    print(captcha_id)
    print(captcha_url)
    captcha_text = input('Please input the captcha:')
    formdata['captcha-solution'] = captcha_text
    formdata['captcha-id'] = captcha_id
    r = s.post(url_login, data = formdata, headers = headers)
with open('contacts.txt', 'w+', encoding = 'utf-8') as f:
    f.write(r.text)
```

或者用cookie登录(cookie是登录了？)
第一种方式总是失败，还是第二个用cookie好用。
爬这些数据不用登录，我一开始403只是没有设置Referer的header而已。
但是学会可以登录也许以后有用。
