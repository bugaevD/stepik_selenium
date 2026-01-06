import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import shutil

link = 'https://demoqa.com/upload-download'
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)

try:
    browser.get(link)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    folder_name = 'test_uploads'
    folder_path = os.path.join(current_dir, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    txt_file_path = os.path.join(folder_path, 'document.txt')
    with open(txt_file_path, 'w', encoding='utf-8') as file:
        file.write('Наш тестовый файл')

    csv_file_path = os.path.join(folder_path, 'data.csv')
    with open(csv_file_path, 'w', encoding='utf-8') as file:
        file.write('email,name\n')
        file.write('jhkdakhdjsa@mail.ru,Natasha\n')
        file.write('dsagyuads@mail.ru,Dmitry\n')

    png_file_path = os.path.join(folder_path, 'image.png')
    with open(png_file_path, 'w', encoding='utf-8') as file:
        file.write('Тестовый png файл\n')
        file.write('Для загрузки сойдет\n')

    upload_button = browser.find_element(By.ID, 'uploadFile')
    upload_button.send_keys(txt_file_path)

    files_to_upload = [txt_file_path, csv_file_path, png_file_path]

    for file in files_to_upload:
        upload_button = wait.until(
            EC.presence_of_element_located((By.ID, 'uploadFile'))
        )
        upload_button.send_keys(file)
        file_name = os.path.basename(file)

        time.sleep(2)

        successful_upload = browser.find_element(By.ID, 'uploadedFilePath').text
        print(f'{file_name}: {successful_upload}')
        assert successful_upload == rf'C:\fakepath\{file_name}'
finally:
    time.sleep(5)
    browser.quit()
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
        print(f'Папка {folder_name} удалена')
    else:
        print(f'Такой папки {folder_name} не существует')

