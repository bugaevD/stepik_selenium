from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


link = 'https://demoqa.com/alerts'
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)

try:
    browser.get(link)
    browser.find_element(By.ID, 'promtButton').click()
    alert = browser.switch_to.alert
    alert.send_keys('Dmitry')
    alert.accept()

finally:
    time.sleep(5)
    browser.quit()