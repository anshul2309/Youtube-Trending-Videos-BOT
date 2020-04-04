from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome('/Users/anshulsharma/Downloads/chromedriver')
driver.get("http://www.youtube.com")
time.sleep(1)
element = driver.find_element_by_xpath('//*[@id="guide-icon"]').click()
time.sleep(1)
element = driver.find_element_by_xpath('/html/body/ytd-app/div/app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[1]/div/ytd-guide-entry-renderer[2]/a/paper-item/yt-formatted-string').click()
time.sleep(3)
driver.close()
