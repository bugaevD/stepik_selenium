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
    first_alert_button = browser.find_element(By.ID, 'alertButton')
    first_alert_button.click()
    alert = browser.switch_to.alert
    print(f'Текст alert: {alert.text}')
    alert.accept()
    print('Alert принят')

    second_alert_button = browser.find_element(By.ID, 'timerAlertButton')
    second_alert_button.click()
    alert = wait.until(EC.alert_is_present())
    print(f'Текст alert: {alert.text}')
    alert.accept()
    print('Alert  задержкой принят')

    third_alert_button = browser.find_element(By.ID, 'confirmButton')
    third_alert_button.click()
    alert = browser.switch_to.alert
    print(f'Текст alert: {alert.text}')
    # alert.accept()
    # result = browser.find_element(By.ID, 'confirmResult').text
    # print(f'{result}')
    alert.dismiss()
    result = browser.find_element(By.ID, 'confirmResult').text
    print(f'{result}')

    fourth_alert_button = browser.find_element(By.ID, 'promtButton')
    fourth_alert_button.click()
    alert = browser.switch_to.alert
    alert.send_keys('Dmitry')
    alert.accept()
    result = browser.find_element(By.ID, 'promptResult').text
    print(f'{result}')


finally:
    time.sleep(5)
    browser.quit()


