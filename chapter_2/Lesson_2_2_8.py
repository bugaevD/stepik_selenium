from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(link)

try:
    browser.find_element(By.CSS_SELECTOR, '.form-group [name="firstname"]').send_keys('Dmitry')
    browser.find_element(By.CSS_SELECTOR, '.form-group [name="lastname"]').send_keys('Bugaev')
    browser.find_element(By.CSS_SELECTOR, '.form-group [name="email"]').send_keys('test@mail.ru')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_dir = os.path.join(current_dir, 'test.txt')
    appload_button = browser.find_element(By.CSS_SELECTOR, 'input#file')
    appload_button.send_keys(file_dir)
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

finally:
    time.sleep(5)
    browser.quit()