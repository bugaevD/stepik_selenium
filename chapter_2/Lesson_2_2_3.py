from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = 'https://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()
browser.get(link)

try:

    num1 = browser.find_element(By.ID, 'num1').text
    num2 = browser.find_element(By.ID, 'num2').text
    numbers_sum = int(num1) + int(num2)
    print(numbers_sum)
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(str(numbers_sum))
    browser.find_element(By.CSS_SELECTOR, 'button.btn-default').click()
finally:
    time.sleep(5)
    browser.quit()
