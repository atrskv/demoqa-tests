import os.path
import time

from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



current_dir = os.path.dirname(os.path.abspath(__file__)) # возвращает абсолютный путь где скрипт исполнялся

# Апгрейдим вебдрайвер, иначе будет качать в директорию вебдрайвера
options = webdriver.ChromeOptions()

prefs = {
    "download.default_directory": os.path.join(current_dir + '/files'),  # с помощью join нормализуем пути
    "download.prompt_for_download": False
} # чтобы не спрашивал подтверждение загрузки

options.add_experimental_option("prefs", prefs)


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Передаем в селен
browser.config.driver = driver

browser.open('https://demoqa.com/upload-download')
browser.element('#downloadButton').click()

# browser.config.hold_browser_open = True
# browser.open('https://demoqa.com/upload-download')
# browser.element("#downloadButton").click()

# prefs = {
#     "download.default_directory": os.path.join(current_dir, 'tmp'),
#     "download.prompt_for_download": False
# }

assert os.path.getsize('files/sampleFile.jpeg') == 4096 # в кб

# os.remove('files/sampleFile.jpeg')