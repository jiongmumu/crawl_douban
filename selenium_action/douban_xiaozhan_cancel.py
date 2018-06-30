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


browser.get('https://www.douban.com/people/shamumu/contact_site')
elements = browser.find_element(By.CLASS_NAME, 'user-list').find_elements_by_tag_name('li')
for ele in elements:
    span_href = ele.find_element_by_tag_name("span")
    span_href.click()
