from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# move firefox profile to ./profile
# https://support.mozilla.org/zh-CN/questions/856113
# Help > Troubleshooting Information > Profile Directory: Open Containing Folder
i = 0
firefox_profile = webdriver.FirefoxProfile('./profile/')
browser = webdriver.Firefox(firefox_profile)
cache = browser.application_cache
# test one
# browser.get("https://www.douban.com/people/63391495/")
# attention_link = browser.find_element(By.CLASS_NAME, 'mr10')
# attention_link.click()
# time.sleep(3)
# print('关注成功')


# browser.get('https://www.douban.com/people/cynthia717/contacts')
# elements = browser.find_elements(By.CLASS_NAME, 'nbg')
# #elements = driver.find_elements_by_class_name('nbg')
# names = []
# for ele in elements:
#     #print(i)
#     #i = i + 1
#     names.append(ele.get_attribute("href"))
#     #ele.click()
# print(names)

#my_amazon_ebooks = 'https://www.amazon.cn/mn/dcw/myx.html/ref=kinw_myk_redirect#/home/content/booksAll/dateDsc/'
sydney_flatmates = 'https://flatmates.com.au/rooms/sydney'
loop = 0
#browser.set_page_load_timeout(20)
browser.get(sydney_flatmates)
time.sleep(2)
rooms = browser.find_elements(By.CLASS_NAME, 'gmnoprint')
print('rooms count:', len(rooms))
for room in rooms:
    room.click()
    time.sleep(2)
