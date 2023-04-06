"""Работа с календарём"""
import time
import datetime
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service('D:\\Projects\\PythonSelenium\\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)
base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
driver.maximize_window()

# Находим наш календарь на сайте
new_date = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")

# Очищаем поле с датой, т.к. в нем уже есть некая информация
new_date.send_keys(Keys.CONTROL + "a")
new_date.send_keys(Keys.BACKSPACE)
time.sleep(3)

# Помещаем новое значение в поле с календарём
new_date.send_keys("12/07/2021")
time.sleep(3)

# Нажимаем ввод чтобы дата сохранилась в поле с календарём
new_date.send_keys(Keys.RETURN)
time.sleep(2)

# Выберем дату в календаре
new_date.click()
time.sleep(2)
december_date = driver.find_element(By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--023']")
december_date.click()
time.sleep(2)

#Выберем дату в текущем месяце текущего года
new_date.click()
new_date.send_keys(Keys.CONTROL + "a")
new_date.send_keys(Keys.BACKSPACE)
new_date.send_keys("11/01/2022")
time.sleep(3)
# Выбираем сегодняшнюю дату с помощью contains(), мы возьмём часть XPATH
new_date.click()
time.sleep(3)
today_date = driver.find_element(By.XPATH, "//div[contains(@class,'react-datepicker__day--today')]")
today_date.click()
time.sleep(2)

#Текущая дата
now_date = datetime.datetime.utcnow().strftime("%d")
print(now_date)

# Переведём текущую дату в числовой тип данных и прибавим один день чтобы получить завтрашнюю дату
int_date = int(now_date) + 1
print(int_date)

# Форматируем дату в нужный формат локатора
if len(str(int_date)) == 1:
    int_date = "00" + str(int_date)
else:
    int_date = "0" + str(int_date)

print(int_date)

# Создадим переменную локатор и присвоим ей следующее значение
locator = "//div[contains(@class, 'react-datepicker__day react-datepicker__day--" + str(int_date) + "')]"
print(locator)

# Получаем завтрашнюю дату
driver.refresh() # обновляем страницу
time.sleep(4)
old_date = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
old_date.click()
time.sleep(2)
date_04 = driver.find_element(By.XPATH, locator)
date_04.click()
