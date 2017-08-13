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
my_amazon_ebooks = 'https://www.amazon.cn/mn/dcw/myx.html/ref=kinw_myk_redirect#/home/content/pdocs/dateDsc/'
loop = 0
#browser.set_page_load_timeout(20)
browser.get(my_amazon_ebooks)
time.sleep(5)
while(1):
    loop = loop + 1
    print('loop:', loop)
    if loop%7 ==0:
        browser.refresh()
        time.sleep(5)
    book_row_elements = browser.find_elements(By.CLASS_NAME, 'myx-fixed-left-grid-inner')
    print('books num:', len(book_row_elements))
    i = 0
    select_num = 0
    to_delete_book_substr = 'Kindle4RSS'
    my_email = 'lxia617@163.comxxxx'
    # select 10 
    for book_row in book_row_elements:
        if select_num >= 10:
            break
        try:
            book_title = book_row.find_element(By.CLASS_NAME, 'myx-color-base')
            if book_title:
                # if title contains certain word
                # if book_title.get_attribute("title").find(to_delete_book_substr) >=0 :
                # not delete my books
                if book_row.get_attribute('innerHTML').find(my_email) == -1:
                    print("select book:" + ":" + book_title.get_attribute("title"))
                    book_title.click()
                    select_num = select_num + 1
        except Exception as ex:
            print(ex)
    # click delete button
    try:
        delete_elem = browser.find_element(By.ID, 'contentAction_delete_myx')
        delete_elem.click()
    except Exception as ex:
        print(ex)
    # click ok button to confirm delete
    try:
        delete_elem = browser.find_element(By.ID, 'dialogButton_ok_myx')
        delete_elem.click()
    except Exception as ex:
        print(ex)
    # click ok button again to let the dialog disappear
    # It will take a while to let the dialog pop up
    time.sleep(8)
    try:
        delete_elem = browser.find_element(By.ID, 'dialogButton_ok_myx')
        delete_elem.click()
    except Exception as ex:
        print(ex)




