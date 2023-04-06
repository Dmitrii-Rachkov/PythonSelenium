import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

"""Открываем сайт с radio button"""
service_obj = Service('D:\\Projects\\PythonSelenium\\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)
base_url = 'https://demoqa.com/radio-button'
driver.get(base_url)
driver.maximize_window()
time.sleep(3)

"""Ищем нашу radio yes кнопку, нажимаем её"""
yes_button = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
yes_button.click()

"""Предположим мы ожидали получить сообщение No вместо Yes при нажатии кнопки Yes"""
try:
    message = driver.find_element(By.XPATH, "//span[@class='text-success']")
    value_message = message.text
    print(value_message)
    assert value_message == "No"
except AssertionError:
    print("Find Assert Exception")
    driver.refresh()
    yes_button = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
    yes_button.click()
    message = driver.find_element(By.XPATH, "//span[@class='text-success']")
    value_message = message.text
    print(value_message)
    assert value_message == "Yes"
print("Assert is GOOD")
