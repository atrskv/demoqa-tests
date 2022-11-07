import os.path

import requests
from requests import Response

r: Response = requests.get('https://selenium.dev/images/selenium_logo_square_green.png')

# функция создания файла в питоне
f = open('selenium.png', 'wb')  # write bytes, так как картинка
f.write(r.content)
f.close()  # открыта на запись, закрываем этой строчкой

print(os.path.getsize('selenium.png'))  # можно использовать при написании асерта

