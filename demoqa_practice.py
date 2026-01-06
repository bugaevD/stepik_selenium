from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'https://demoqa.com/automation-practice-form'
browser = webdriver.Chrome()
browser.implicitly_wait(5)
try:
    browser.get(link)
    browser.find_element(By.ID, 'firstName').send_keys('Dmitry')
    browser.find_element(By.ID, 'lastName').send_keys('Bugaev')
    browser.find_element(By.ID, 'userEmail').send_keys('test@mail.ru')
    browser.find_element(By.CSS_SELECTOR, '[name="gender"][value="Male"] + label').click()
    browser.find_element(By.ID, 'userNumber').send_keys('8911111111')
    # browser.find_element(By.ID, 'dateOfBirthInput').set
finally:
    time.sleep(5)
    browser.quit()
