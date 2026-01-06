from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

url = 'http://suninjuly.github.io/find_link_text'
browser = webdriver.Chrome()
browser.get(url)

try:
    link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()
    input_1 = browser.find_element(By.NAME, 'first_name')
    input_1.send_keys('Dmitry')
    input_2 = browser.find_element(By.NAME, 'last_name')
    input_2.send_keys('Bugaev')
    input_3 = browser.find_element(By.CLASS_NAME, 'city')
    input_3.send_keys('Saint-Petersburg')
    input_4 = browser.find_element(By.ID, 'country')
    input_4.send_keys('Russia')
    submit_button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    submit_button.click()
finally:
    time.sleep(5)
    browser.quit()