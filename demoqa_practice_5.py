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
    test_data = [
        ('Dmitry', 'Dmitry'),
        ('12345', '12345')
    ]
    promt_button = browser.find_element(By.ID, 'promtButton')

    for i, (data_to_type, expected) in enumerate(test_data, 1):
        print(f'Провожу тест номер {i}, с данными {data_to_type}')

        promt_button.click()
        alert = browser.switch_to.alert
        alert.send_keys(data_to_type)
        alert.accept()

        time.sleep(1)
        result = browser.find_element(By.ID, 'promptResult').text
        print(f'Ожидалось')

        assert expected in result

finally:
    time.sleep(5)
    browser.quit()