import datetime
import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

"""Открываем сайт с календарём"""
service_obj = Service('D:\\Projects\\PythonSelenium\\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)
base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
driver.maximize_window()
time.sleep(3)

"""Узнаём текущую дату"""
now_date = datetime.date.today()
print(now_date)

"""Создаём искомую дату от текущей + 10 дней"""
target_date = now_date + datetime.timedelta(days=10)
print(target_date)

"""Форматируем найденную дату в формат для вставки на сайте в поле Select Date"""
format_target_date = target_date.strftime("%m/%d/%Y")
print(format_target_date)

"""Находим поле Select Date на сайте и очищаем его"""
select_date = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
select_date.send_keys(Keys.CONTROL + "a")
select_date.send_keys(Keys.BACKSPACE)
time.sleep(3)

"""Вставляем нашу искомую дату + 10 дней"""
select_date.send_keys(format_target_date)
select_date.send_keys(Keys.RETURN)
time.sleep(2)

"""Проверяем что наша искомая дата введена в поле Select Date"""
actual_date = select_date.get_attribute('value') # текущее значение поля
assert format_target_date == actual_date
print("Home work is Completed")

