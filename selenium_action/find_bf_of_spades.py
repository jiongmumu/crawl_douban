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


browser.get('https://www.douban.com/people/gotohell/contacts')
elements = browser.find_elements(By.CLASS_NAME, 'nbg')
#elements = driver.find_elements_by_class_name('nbg')
names = []
for ele in elements:
    #print(i)
    #i = i + 1
    names.append(ele.get_attribute("href"))
    #ele.click()
print(names)

#names = []
france_i = 0
for name in reversed(names):
    browser.get(name)
    user_info_div = browser.find_element(By.CLASS_NAME, 'user-info')
    #attention_link = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "a-btn-add mr10 add_contact")))
    if user_info_div:
        user_info = user_info_div.text
        if user_info.lower().find('france') != -1 or user_info.lower().find('france') !=-1:
            print(france_i)
            print(name)
            france_i = france_i + 1
#element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))
#elem.send_keys('seleniumhq' + Keys.RETURN)

#driver.quit()