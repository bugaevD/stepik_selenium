from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

link = 'https://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, 'button.trollface').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(1)
    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(y)
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    print(browser.switch_to.alert.text.split(': ')[-1])
finally:
    time.sleep(5)
    browser.quit()