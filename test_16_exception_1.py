import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

"""Открываем сайт с динамическими элементами"""
service_obj = Service('D:\\Projects\\PythonSelenium\\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)
base_url = 'https://demoqa.com/dynamic-properties'
driver.get(base_url)
driver.maximize_window()
time.sleep(3)

"""Ищем нашу visible кнопку, нажимаем её и обрабатыаем исключение"""
try:
    visible_button = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
    visible_button.click()
except NoSuchElementException as exception:
    print("NoSuchElementException is find")
    time.sleep(5)
    visible_button = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
    visible_button.click()
    print("Click Visivle Button")
