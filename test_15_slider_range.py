import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

"""Открываем сайт с ползунком"""
service_obj = Service('D:\\Projects\\PythonSelenium\\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)
base_url = 'https://html5css.ru/howto/howto_js_rangeslider.php'
driver.get(base_url)
driver.maximize_window()
time.sleep(3)

action = ActionChains(driver)  # для работы с мышью я так понял
slider_square = driver.find_element(By.XPATH, "//input[@class='slider-square']")
# action.click_and_hold(slider_square) - клик мышкой и удержание
# move_by_offset(20, 0) - перемещение по оси X и Y
# release() - отпустить кнокпку мыши
# perform - сохранить результат
action.click_and_hold(slider_square).move_by_offset(0, 20).release().perform()
print("Slider-square is active")
