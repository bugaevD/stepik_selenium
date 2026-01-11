from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

def test_first_page():
    try:
        link = 'http://suninjuly.github.io/registration1.html'
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element(By.CSS_SELECTOR, '.first_block .first_class input')
        first_name.send_keys('Dmitry')
        last_name = browser.find_element(By.CSS_SELECTOR, '.first_block .second_class input')
        last_name.send_keys('Bugaev')
        email = browser.find_element(By.CSS_SELECTOR, '.first_block .third_class input')
        email.send_keys('bbbbb@mail.ru')
        submit_button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
        submit_button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')
        welcome_text = welcome_text_elt.text

        assert 'Congratulations! You have successfully registered!' == welcome_text
    finally:
        time.sleep(5)
        browser.quit()

def test_second_page():
    try:
        link = 'http://suninjuly.github.io/registration2.html'
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element(By.CSS_SELECTOR, '.first_block .first_class input')
        first_name.send_keys('Dmitry')
        last_name = browser.find_element(By.CSS_SELECTOR, '.first_block .second_class input')
        last_name.send_keys('Bugaev')
        email = browser.find_element(By.CSS_SELECTOR, '.first_block .third_class input')
        email.send_keys('bbbbb@mail.ru')
        submit_button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
        submit_button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')
        welcome_text = welcome_text_elt.text

        assert 'Congratulations! You have successfully registered!' == welcome_text
    finally:
        time.sleep(5)
        browser.quit()

if __name__ == '__main__':
    pytest.main()