# https://selenium-python.com/ - гайд по установке selenium
# 'python -m pip install --upgrade pip' - это команда для установки менеджера пакетов
# PIP — это менеджер пакетов для Python. PIP поставляется с установщиком Python
# Если при открытии терминала возникает ошибка, то скорее всего это ошибка PowerShell
# связанная с правами доступа. Вам нужно изменить права доступа в PowerShell.
# Нужно посмотреть права доступа - 'Get-ExecutionPolicy -List'
# Установить новые права доступа - 'Set-ExecutionPolicy Unrestricted'

# Далее устанавливаем selenium. Для этого ввёдём команду в терминале: 'pip3 install selenium'

# Далее для тестирования с помощью браузера chrome нам нужно скачать 'chromedriver'.
# https://chromedriver.chromium.org/downloads - сайт для скачивания
# скачивать нужно ту версию которая у вас в браузере, посмотрите это в настройках
# Далее нужно распаковать архив и засунуть файл в корень вашего проекта

# Тоже самое нужно сделать с geckodriver, здесь скачать - https://github.com/mozilla/geckodriver/releases
# Распаковать и засунуть в проект

# https://pypi.org/project/webdriver-manager/ - решение проблем с webdriver

# импортируем webdriver из selenium
# Для работы с Google Chrome создаём такую переменную с путём к нашему 'chromedriver'.
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='D:\Projects\PythonSelenium\chromedriver.exe')
# driver.get('https://www.saucedemo.com/')


# Вариант выше устарел, можно использовать новый вариант вот так:
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# import time
# service_obj = Service('D:\\Projects\\PythonSelenium\\chromedriver.exe')
# driver = webdriver.Chrome(service=service_obj)
# # Далее открываем наш тестируемы файл
# driver.get('https://www.saucedemo.com/')
# # Изменяем размер открываемой вкладки нашего сайта
# driver.maximize_window()
# # Чтобы сделать задержку перед закрытием браузера выполняем команду и импортируем пакет:
# time.sleep(10)
# # Чтобы закрыть браузер пишем команду:
# driver.close()

# Для Firefox используем следующее:
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
service_obj = Service('D:\\Projects\\PythonSelenium\\geckodriver.exe')
driver = webdriver.Firefox(service=service_obj)
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
time.sleep(10)
driver.close()

