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


#browser.get('https://www.douban.com/group/people/shamumu/joins')
#elements = browser.find_element(By.CLASS_NAME, 'group-list').find_elements(By.CLASS_NAME, 'title')
# groups = []
# for ele in elements:
#     a_href = ele.find_element_by_tag_name("a")
#     groups.append(a_href.get_attribute("title"))
#     groups.append(a_href.get_attribute("href"))
# print(groups)

groups = []

i = 0
while i < len(groups) - 1:
    time.sleep(3)
    browser.get(groups[i+1])
    i = i + 2
    try:
        cancel_div = browser.find_element(By.CLASS_NAME, 'group-misc')
        #attention_link = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "a-btn-add mr10 add_contact")))
        if cancel_div:
            cancel_link = cancel_div.find_element_by_tag_name('a')
            if cancel_link.text.find('退出') != -1:
                cancel_link.click()
                #time.sleep(3)
                try:
                    print('click exit')
                    # WebDriverWait(browser, 3).until(EC.alert_is_present(),
                    #                                '真的要退出小组?')
                    alert = browser.switch_to.alert
                    print('text:', alert.text)
                    alert.accept()
                    print("click alert")
                except TimeoutException:
                    print("no alert")
                print(groups[i-2]  + "  成功取消")
    except:
        print(groups[i-2] + " 失败")

#driver.quit()