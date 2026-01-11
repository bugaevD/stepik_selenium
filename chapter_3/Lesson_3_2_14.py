import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRegistrationForm(unittest.TestCase):
    def test_complete_form1(self):
        link = 'http://suninjuly.github.io/registration2.html'
        browser = webdriver.Chrome()
        browser.get(link)
        try:
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
        finally:
            time.sleep(5)
            browser.quit()
        self.assertEqual('Congratulations! You have successfully registered!', welcome_text, 'Текст не совпадает')
    def test_complete_form2(self):
        link = 'http://suninjuly.github.io/registration1.html'
        browser = webdriver.Chrome()
        browser.get(link)
        try:
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

            self.assertEqual('Congratulations! You have successfully registered!', welcome_text, 'Текст не совпадает')

        finally:
            time.sleep(5)
            browser.quit()
if __name__ == '__main__':
        unittest.main()


