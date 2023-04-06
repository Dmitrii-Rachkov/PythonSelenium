# Ещё сайт для тренировки https://demoqa.com/
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service('D:\\Projects\\PythonSelenium\\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)
base_url = 'https://demoqa.com/checkbox' # наш сайт поместим в переменную и будем использовать её дальше
driver.get(base_url)
driver.maximize_window()

# Нажимаем чек-бокс
checkbox = driver.find_element(By.XPATH, "//span[@class='rct-checkbox']")
checkbox.click()
time.sleep(2)

# Распахиваем главное дерево
expand_main = driver.find_element(By.XPATH, "//button[@aria-label='Toggle']")
expand_main.click()
time.sleep(2)

# Отжимаем главный чек-бокс
checkbox.click()

# Ещё сайт для тренировки: https://testpages.herokuapp.com/styled/basic-html-form-test.html