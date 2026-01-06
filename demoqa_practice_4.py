# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# link = 'https://demoqa.com/alerts'
# browser = webdriver.Chrome()
# wait = WebDriverWait(browser, 10)
#
# try:
#     browser.get(link)
#     confirm_button_alert = browser.find_element(By.ID, 'confirmButton')
#     confirm_button_alert.click()
#     alert = browser.switch_to.alert
#     print(f'{alert.text}')
#     alert.accept()
#     result = browser.find_element(By.ID, 'confirmResult').text
#     print(f'{result}')
#
#     assert 'Ok' in result, f'Ожидалось "Ok", получено {result}'
#
#     confirm_button_alert.click()
#     alert = browser.switch_to.alert
#     print(f'{alert.text}')
#     alert.dismiss()
#     result = browser.find_element(By.ID, 'confirmResult').text
#     print(f'{result}')
#
#     assert 'Cancel' in result, f'Ожидалось "Ok", получено {result}'
#
# finally:
#     time.sleep(5)
#     browser.quit()